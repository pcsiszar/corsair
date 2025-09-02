package org.pcsiszar.corsair.test;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.pcsiszar.corsair.character.Attribute;
import org.pcsiszar.corsair.character.AttributePair;
import org.pcsiszar.corsair.dice.TestDie;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ComplexTestTest {

  private AttributePair attributePair;

  @BeforeEach
  void setUp() {
    attributePair = new AttributePair();
    attributePair.setFirst(new Attribute("Test1", 4));
    attributePair.setSecond(new Attribute("Test2", 2));
  }

  @Test
  void testSuccessfulComplexTest() {
    // Given
    ComplexTest complexTest = new ComplexTest(attributePair, () -> new TestDie(10));
    // This will make the dice roll 8, 7, 6, 5
    ((TestDie) complexTest.dicePool.getDice().get(0)).setNextRoll(8);
    ((TestDie) complexTest.dicePool.getDice().get(1)).setNextRoll(7);
    ((TestDie) complexTest.dicePool.getDice().get(2)).setNextRoll(6);
    ((TestDie) complexTest.dicePool.getDice().get(3)).setNextRoll(5);

    // When
    complexTest.roll();
    complexTest.progress();
    // This will make the dice roll 9, 1
    ((TestDie) complexTest.dicePool.getDice().get(0)).setNextRoll(9);
    ((TestDie) complexTest.dicePool.getDice().get(1)).setNextRoll(1);
    complexTest.roll();
    ComplexResult result = complexTest.resolve();

    // Then
    assertEquals(ResultCategory.SUCCESS, result.resultCategory());
    assertEquals(9, result.successPoints());
  }

  @Test
  void testFailedComplexTest() {
    // Given
    ComplexTest complexTest = new ComplexTest(attributePair, () -> new TestDie(10));
    // This will make the dice roll 7, 6, 5, 4
    ((TestDie) complexTest.dicePool.getDice().get(0)).setNextRoll(7);
    ((TestDie) complexTest.dicePool.getDice().get(1)).setNextRoll(6);
    ((TestDie) complexTest.dicePool.getDice().get(2)).setNextRoll(5);
    ((TestDie) complexTest.dicePool.getDice().get(3)).setNextRoll(4);

    // When
    complexTest.roll();
    complexTest.progress();
    ComplexResult result = complexTest.resolve();

    // Then
    assertEquals(ResultCategory.FAILURE, result.resultCategory());
    assertEquals(0, result.successPoints());
  }

  @Test
  void testSuccessfulComplexTestWithBonus() {
    // Given
    ComplexTest complexTest = new ComplexTest(attributePair, () -> new TestDie(10));
    complexTest.setSuccessBonus(5);
    // This will make the dice roll 8, 7, 6, 5
    ((TestDie) complexTest.dicePool.getDice().get(0)).setNextRoll(8);
    ((TestDie) complexTest.dicePool.getDice().get(1)).setNextRoll(7);
    ((TestDie) complexTest.dicePool.getDice().get(2)).setNextRoll(6);
    ((TestDie) complexTest.dicePool.getDice().get(3)).setNextRoll(5);

    // When
    complexTest.roll();
    complexTest.progress();
    // This will make the dice roll 9, 1
    ((TestDie) complexTest.dicePool.getDice().get(0)).setNextRoll(9);
    ((TestDie) complexTest.dicePool.getDice().get(1)).setNextRoll(1);
    complexTest.roll();
    ComplexResult result = complexTest.resolve();

    // Then
    assertEquals(ResultCategory.SUCCESS, result.resultCategory());
    assertEquals(14, result.successPoints());
  }

  @Test
  void testFailedComplexTestWithBonus() {
    // Given
    ComplexTest complexTest = new ComplexTest(attributePair, () -> new TestDie(10));
    complexTest.setSuccessBonus(5);
    // This will make the dice roll 7, 6, 5, 4
    ((TestDie) complexTest.dicePool.getDice().get(0)).setNextRoll(7);
    ((TestDie) complexTest.dicePool.getDice().get(1)).setNextRoll(6);
    ((TestDie) complexTest.dicePool.getDice().get(2)).setNextRoll(5);
    ((TestDie) complexTest.dicePool.getDice().get(3)).setNextRoll(4);

    // When
    complexTest.roll();
    complexTest.progress();
    ComplexResult result = complexTest.resolve();

    // Then
    assertEquals(ResultCategory.FAILURE, result.resultCategory());
    assertEquals(0, result.successPoints());
  }
}
