package org.pcsiszar.corsair.dice;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class DieTest {

  @Test
  void testDieRoll() {
    Die die = Die.d10();
    Map<Long, Long> resultMap = new HashMap<>();
    for (int i = 0; i < 1000000; i++) {
      long result = die.roll();
      resultMap.put(result, resultMap.computeIfAbsent(result, (__) -> 0L) + 1);
    }
    Assertions.assertEquals(Set.of(1L, 2L, 3L, 4L, 5L, 6L, 7L, 8L, 9L, 10L), resultMap.keySet());
  }
}
