package org.pcsiszar.corsair.roll;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import org.pcsiszar.corsair.dice.DicePool;
import org.pcsiszar.corsair.dice.Die;

import java.util.stream.IntStream;

public class ActionRollTest {

  @ParameterizedTest
  @ValueSource(ints = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 })
  void calcProbabilities(int value) {
    tenThouWithD(value, 8);
    tenThouWithD(value, 10);
    tenThouWithD(value, 12);
  }

  private static void tenThouWithD(int value, int face) {
    int runs = 100000;
    int fullSuccess = 0;
    int mixedSuccess = 0;
    int pointsOnFullSuccess = 0;
    int pointsOnMixedSuccess = 0;

    for (int i = 0; i < runs; i++) {
      DicePool dicePool =
          new DicePool(IntStream.range(0, value).mapToObj(__ -> new Die(face)).toList());
      ActionResult result = ActionRoll.rollAction(dicePool);
      if (result.resultCategory() == ResultCategory.FULL_SUCCESS) {
        fullSuccess++;
        pointsOnFullSuccess += result.points();
      } else if (result.resultCategory() == ResultCategory.MIXED_SUCCESS) {
        mixedSuccess++;
        pointsOnMixedSuccess += result.points();
      }
    }
    System.out.println("Rolling " + value + "," + face + " sided dice");
    System.out.println("Full Success:" + ((double) fullSuccess * 100 / runs) + "%");
    System.out.println(
        "Full Success average points:" + ((double) pointsOnFullSuccess / fullSuccess));
    System.out.println("Mixed Success:" + ((double) mixedSuccess * 100 / runs) + "%");
    System.out.println(
        "Mixed Success expected points:" + ((double) pointsOnMixedSuccess / mixedSuccess));
  }

}
