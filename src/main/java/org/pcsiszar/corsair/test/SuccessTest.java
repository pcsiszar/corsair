package org.pcsiszar.corsair.test;

import org.pcsiszar.corsair.dice.DicePool;
import org.pcsiszar.corsair.dice.Die;

import java.util.Comparator;

public class SuccessTest extends Test<SuccessResult> {
  public SuccessTest(DicePool dicePool) {
    super(dicePool);
  }

  @Override
  public SuccessResult evaluate() {
    return new SuccessResult(
        dicePool.getDice().stream()
            .map(Die::getValue)
            .max(Comparator.naturalOrder())
            .orElse(0));
  }
}
