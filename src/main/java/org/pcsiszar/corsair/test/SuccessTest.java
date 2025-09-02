package org.pcsiszar.corsair.test;

import org.pcsiszar.corsair.character.AttributePair;
import org.pcsiszar.corsair.dice.DicePool;
import org.pcsiszar.corsair.dice.Die;

import java.util.Comparator;

public class SuccessTest extends Test<SuccessResult> {

  private int successBonus = 0;

  public SuccessTest(AttributePair attributePair) {
    super(attributePair);
  }

  @Override
  protected DicePool getInitialDicePool(AttributePair attributePair) {
    return DicePool.ofSize(attributePair.getLower().getValue());
  }

  @Override
  public SuccessResult evaluate() {
    return new SuccessResult(
        dicePool.getDice().stream()
            .map(Die::getValue)
            .max(Comparator.naturalOrder())
            .orElse(0) + successBonus);
  }

  public void setSuccessBonus(int successBonus) {
    this.successBonus = successBonus;
  }
}
