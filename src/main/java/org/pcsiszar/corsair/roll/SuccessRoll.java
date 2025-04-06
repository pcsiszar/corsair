package org.pcsiszar.corsair.roll;

import org.pcsiszar.corsair.dice.DicePool;
import org.pcsiszar.corsair.dice.Die;

import java.util.Comparator;

public class SuccessRoll {
  public static SuccessResult rollAction(DicePool dicePool) {
    dicePool.roll();

    var points =
        dicePool.getDice().stream().map(SuccessRoll::getPoints).reduce(0, Integer::sum);

    return new SuccessResult(points);
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
