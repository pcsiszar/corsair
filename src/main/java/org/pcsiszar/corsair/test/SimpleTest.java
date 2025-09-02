package org.pcsiszar.corsair.test;

import org.pcsiszar.corsair.character.AttributePair;
import org.pcsiszar.corsair.dice.DicePool;
import org.pcsiszar.corsair.dice.Die;

import java.util.Comparator;

public class SimpleTest extends Test<SimpleResult> {

  private SimpleTest(AttributePair attributePair) {
    super(attributePair);
  }

  @Override
  protected DicePool getInitialDicePool(AttributePair attributePair) {
    return DicePool.ofSize(attributePair.getHigher().getValue());
  }

  @Override
  public SimpleResult evaluate() {
    return getSimpleResult(dicePool);
  }

  public static SimpleResult getSimpleResult(DicePool dicePool) {
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
