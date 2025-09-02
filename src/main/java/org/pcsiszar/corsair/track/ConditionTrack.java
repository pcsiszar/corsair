package org.pcsiszar.corsair.track;

import java.util.List;

/**
 * A special track that consists of three tracks, each progressing sequentially.
 * One track progresses only after the one before is filled.
 * Progress carries over from a filled track to the next.
 */
public class ConditionTrack {

    private final List<Track> tracks;

    /**
     * Constructs a ConditionTrack with three identical sequential tracks.
     * @param trackFinalValue the final value for each of the three tracks
     */
    public ConditionTrack(int trackFinalValue) {
        this.tracks = List.of(
                new Track(trackFinalValue),
                new Track(trackFinalValue),
                new Track(trackFinalValue)
        );
    }

    /**
     * Applies damage to the condition track, increasing its progress.
     * The progress fills the tracks sequentially and carries over.
     * @param amount the amount of damage to apply
     * @return true if the entire condition track is completed, false otherwise
     */
    public boolean damage(int amount) {
        int remainingAmount = amount;
        if (remainingAmount <= 0) {
            return isCompleted();
        }

        for (Track track : tracks) {
            if (!track.isCompleted()) {
                int spaceLeft = track.getFinalValue() - track.getCurrentProgress();
                if (remainingAmount <= spaceLeft) {
                    track.increase(remainingAmount);
                    return isCompleted();
                } else {
                    track.increase(spaceLeft); // Fill up this track
                    remainingAmount -= spaceLeft;
                }
            }
        }
        return isCompleted();
    }

    /**
     * Heals the condition track, decreasing its progress.
     * The progress is removed from the tracks in reverse sequential order.
     * @param amount the amount to heal
     */
    public void heal(int amount) {
        int remainingAmount = amount;
        if (remainingAmount <= 0) {
            return;
        }

        for (int i = tracks.size() - 1; i >= 0; i--) {
            Track track = tracks.get(i);
            int currentProgress = track.getCurrentProgress();

            if (remainingAmount <= currentProgress) {
                track.decrease(remainingAmount);
                return; // All amount used up
            } else {
                track.decrease(currentProgress); // Empty this track's progress
                remainingAmount -= currentProgress;
            }
        }
    }

    /**
     * Checks if the entire condition track is completed.
     * @return true if all tracks are completed, false otherwise
     */
    public boolean isCompleted() {
        return tracks.stream().allMatch(Track::isCompleted);
    }

    /**
     * Gets the list of tracks.
     * @return the list of tracks
     */
    public List<Track> getTracks() {
        return tracks;
    }
}
