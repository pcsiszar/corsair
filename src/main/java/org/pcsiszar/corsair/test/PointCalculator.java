package org.pcsiszar.corsair.test;

import org.pcsiszar.corsair.dice.Die;

public final class PointCalculator {

  private PointCalculator() {

  }

  public static int calculatePoints(Die die) {
    return calculatePoints(die, false);
  }

  public static int calculatePoints(Die die, boolean canCrit) {
    int dieValue = die.getValue();
    if (dieValue == 12 && canCrit) {
      return 4;
    }
    if (dieValue >= 10) {
      return 3;
    }
    if (dieValue >= 7) {
      return 2;
    }
    return 1;
  }
}
