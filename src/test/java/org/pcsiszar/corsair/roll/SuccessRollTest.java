package org.pcsiszar.corsair.roll;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import org.pcsiszar.corsair.dice.DicePool;
import org.pcsiszar.corsair.dice.Die;

import java.util.stream.IntStream;

public class SuccessRollTest {

  @ParameterizedTest
  @ValueSource(ints = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 })
  void calcProbabilities(int value) {
    tenThouWithD(value, 8);
    tenThouWithD(value, 10);
    tenThouWithD(value, 12);
  }

  private static void tenThouWithD(int value, int face) {
    int runs = 100000;
    int points = 0;

    for (int i = 0; i < runs; i++) {
      DicePool dicePool =
          new DicePool(IntStream.range(0, value).mapToObj(__ -> new Die(face)).toList());
      SuccessResult result = SuccessRoll.rollAction(dicePool);
      points += result.points();
    }
    System.out.println("Rolling " + value + "," + face + " sided dice");
    System.out.println(
        "Full Success average points:" + ((double) points / runs));
  }

}
