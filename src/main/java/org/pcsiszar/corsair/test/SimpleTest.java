package org.pcsiszar.corsair.test;

import org.pcsiszar.corsair.dice.DicePool;
import org.pcsiszar.corsair.dice.Die;

import java.util.Comparator;

public class SimpleTest extends Test<SimpleResult> {

  private DicePool dicePool;

  private SimpleTest(DicePool dicePool) {
    super(dicePool);
  }

  @Override
  public SimpleResult evaluate() {
    ResultCategory resultCategory =
        dicePool.getDice().stream().max(Comparator.naturalOrder())
            .map(SimpleTest::evaluateResultCategory)
            .orElse(ResultCategory.FAILURE);

    return new SimpleResult(resultCategory);
  }

  private static ResultCategory evaluateResultCategory(Die die) {
    return die.getValue() >= 8 ? ResultCategory.SUCCESS : ResultCategory.FAILURE;
  }
}
