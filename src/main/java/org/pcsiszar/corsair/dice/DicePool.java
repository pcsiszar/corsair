package org.pcsiszar.corsair.dice;

import java.util.Arrays;
import java.util.List;

public class DicePool {
  private final List<Die> dicePool;

  public static DicePool from(Die... rest) {
    return new DicePool(Arrays.asList(rest));
  }

  public DicePool(List<Die> dicePool) {
    if (dicePool == null || dicePool.isEmpty()) {
      throw new IllegalArgumentException("Cannot create an empty Dice Pool");
    }
    this.dicePool = dicePool;
  }

  public void roll() {
    dicePool.forEach(Die::roll);
  }

  public List<Die> getDice() {
    return dicePool;
  }
}
