package org.pcsiszar.corsair.track;

public class Track {

    private int currentProgress;
    private final int totalProgress;

    public Track(int totalProgress) {
        this.totalProgress = totalProgress;
        this.currentProgress = 0;
    }

    /**
     * Increases the progress of the track.
     *
     * @param amount the amount to increase the progress by
     * @return true if the track is completed, false otherwise
     */
    public boolean increase(int amount) {
        this.currentProgress += amount;
        if (this.currentProgress >= this.totalProgress) {
            this.currentProgress = this.totalProgress;
            return true;
        }
        return false;
    }

    /**
     * Decreases the progress of the track.
     *
     * @param amount the amount to decrease the progress by
     */
    public void decrease(int amount) {
        this.currentProgress -= amount;
        if (this.currentProgress < 0) {
            this.currentProgress = 0;
        }
    }

    public int getCurrentProgress() {
        return currentProgress;
    }

    public int getFinalValue() {
        return totalProgress;
    }


    public boolean isCompleted() {
        return this.currentProgress >= this.totalProgress;
    }
}
