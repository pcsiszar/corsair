package org.pcsiszar.corsair.combat;

import org.pcsiszar.corsair.character.AttributePair;
import org.pcsiszar.corsair.character.Character;
import org.pcsiszar.corsair.test.ComplexResult;
import org.pcsiszar.corsair.test.ComplexTest;
import org.pcsiszar.corsair.test.ResultCategory;
import org.pcsiszar.corsair.test.SimpleResult;

public class Attack {

    private final Character attacker;
    private final Character defender;
    private final AttributePair attributes;
    private ComplexResult result;

    public Attack(Character attacker, Character defender, AttributePair attributes) {
        this.attacker = attacker;
        this.defender = defender;
        this.attributes = attributes;
    }

    public void execute() {
        ComplexTest combatTest = new ComplexTest(attributes);
        combatTest.setSuccessBonus(attacker.getDamageBonus());
        combatTest.roll();
        SimpleResult progress = combatTest.progress();
        if (progress.resultCategory() == ResultCategory.SUCCESS) {
            combatTest.roll();
        }
        this.result = combatTest.resolve();

        int damage = Math.max(0, result.successPoints() - defender.getPhysicalProtection());
        defender.takePhysicalDamage(damage);
    }

    public Character getAttacker() {
        return attacker;
    }

    public Character getDefender() {
        return defender;
    }

    public ComplexResult getResult() {
        return result;
    }
}
