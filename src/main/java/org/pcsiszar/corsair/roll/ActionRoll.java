package org.pcsiszar.corsair.roll;

import org.pcsiszar.corsair.dice.DicePool;
import org.pcsiszar.corsair.dice.Die;

import java.util.Comparator;

public class ActionRoll {

  public static ActionResult rollAction(DicePool dicePool) {
    dicePool.roll();
    ResultCategory resultCategory =
        dicePool.getDice().stream().max(Comparator.naturalOrder())
            .map(ActionRoll::evaluateResultCategory)
            .get();

    if (resultCategory == ResultCategory.FAILURE) {
      return new ActionResult(resultCategory, 0);
    }

    var successDice =
        dicePool.getDice().stream().sorted(Comparator.reverseOrder()).filter(d -> d.getValue() >= 7)
            .toList();

    DicePool successPool = new DicePool(successDice);

    var points =
        successPool.getDice().stream().map(ActionRoll::getPoints).reduce(0, Integer::sum);

    return new ActionResult(resultCategory, points);
  }

  private static ResultCategory evaluateResultCategory(Die die) {
    return switch (die.getValue()) {
      case 12, 11, 10 -> ResultCategory.FULL_SUCCESS;
      case 9, 8, 7 -> ResultCategory.MIXED_SUCCESS;
      default -> ResultCategory.FAILURE;
    };
  }

  private static int getPoints(Die die) {
    return switch (die.getValue()) {
      case 12 -> 4;
      case 11, 10 -> 3;
      case 9, 8, 7 -> 2;
      default -> 1;
    };
  }
}
