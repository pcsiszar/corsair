package org.pcsiszar.corsair.combat;

import org.junit.jupiter.api.Test;
import org.pcsiszar.corsair.character.Character;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class CombatSimulatorTest {

    @Test
    void simulateCombat() {
        int numSimulations = 1000000;
        int blueWins = 0;
        long totalBlueSurvivors = 0;
        long totalBlueHpLeft = 0;
        long totalResets = 0;

        for (int i = 0; i < numSimulations; i++) {
            List<Character> blueTeam = createTeam(3);
            List<Character> redTeam = createTeam(3);

            CombatSimulator simulator = new CombatSimulator(new ArrayList<>(blueTeam), new ArrayList<>(redTeam));
            simulator.simulate();

            if (redTeam.stream().allMatch(c->c.getPhysicalTrack().isCompleted())) {
                blueWins++;
                totalBlueSurvivors += blueTeam.size();
                totalBlueHpLeft += blueTeam.stream().mapToInt(Character::getRemainingPhysicalHp).sum();
            }
            totalResets += simulator.getResetCount();
        }

        double blueWinPercentage = (double) blueWins / numSimulations * 100;
        double avgBlueSurvivors = (double) totalBlueSurvivors / numSimulations;
        double avgBlueHpLeft = (double) totalBlueHpLeft / numSimulations;
        double avgResets = (double) totalResets / numSimulations;

        System.out.println("Combat Simulation Results (" + numSimulations + " runs):");
        System.out.println("Blue Team Win Percentage: " + String.format("%.2f", blueWinPercentage) + "%");
        System.out.println("Average Blue Team Survivors: " + String.format("%.2f", avgBlueSurvivors));
        System.out.println("Average Blue Team HP Left: " + String.format("%.2f", avgBlueHpLeft));
        System.out.println("Average Resets per Combat: " + String.format("%.2f", avgResets));
    }

    private List<Character> createTeam(int size) {
        return IntStream.range(0, size)
                .mapToObj(i -> Character.builder().str(5).agi(4).fin(3).knw(3).pre(3).ins(3).build())
                .collect(Collectors.toList());
    }
}
