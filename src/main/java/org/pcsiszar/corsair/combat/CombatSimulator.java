package org.pcsiszar.corsair.combat;

import lombok.Getter;
import org.pcsiszar.corsair.character.AttributePair;
import org.pcsiszar.corsair.character.Character;

import java.util.Comparator;
import java.util.List;
import java.util.Optional;

public class CombatSimulator {

    private final List<Character> blueTeam;
    private final List<Character> redTeam;
    @Getter
    private int resetCount = 0;

    public CombatSimulator(List<Character> blueTeam, List<Character> redTeam) {
        this.blueTeam = blueTeam;
        this.redTeam = redTeam;
    }

    public void simulate() {
        boolean isBlueTurn = true;

        while (!blueTeam.isEmpty() && !redTeam.isEmpty()) {
            if (isBlueTurn) {
                performTeamAttack(blueTeam, redTeam);
            } else {
                performTeamAttack(redTeam, blueTeam);
            }

            isBlueTurn = !isBlueTurn;

            if (!teamCanAct(blueTeam) && !teamCanAct(redTeam)) {
                resetActionTokens(blueTeam);
                resetActionTokens(redTeam);
                resetCount++;
            }
        }
    }

    private void performTeamAttack(List<Character> attackingTeam, List<Character> defendingTeam) {
        Optional<Character> attackerOpt = findAttacker(attackingTeam);
        if (attackerOpt.isEmpty()) {
            return; // No one can attack
        }
        Character attacker = attackerOpt.get();

        Optional<Character> targetOpt = findTarget(defendingTeam);
        if (targetOpt.isEmpty()) {
            return; // No one to attack
        }
        Character target = targetOpt.get();

        AttributePair attributes = new AttributePair();
        attributes.setFirst(attacker.getStrength());
        attributes.setSecond(attacker.getAgility());

        Attack attack = attacker.declareAttack(target, attributes);
        attack.execute();

        if (target.getPhysicalTrack().isCompleted()) {
            defendingTeam.remove(target);
        }
    }

    private Optional<Character> findAttacker(List<Character> team) {
        return team.stream().filter(c -> c.getActionTokens() >= 2).findFirst();
    }

    private Optional<Character> findTarget(List<Character> team) {
        return team.stream().max(Comparator.comparingInt(Character::getTotalPhysicalDamage));
    }

    private boolean teamCanAct(List<Character> team) {
        return team.stream().anyMatch(c -> c.getActionTokens() >= 2);
    }

    private void resetActionTokens(List<Character> team) {
        team.forEach(c -> c.setActionTokens(4));
    }

}

