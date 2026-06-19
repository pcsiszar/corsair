package org.pcsiszar.corsair.test;

import org.junit.jupiter.api.Test;
import org.pcsiszar.corsair.character.Attribute;
import org.pcsiszar.corsair.character.AttributePair;

class MonteCarloTest {

  private static final int ITERATIONS = 50000;

  @Test
  void runSimpleTestSimulation() {
    System.out.println(
        "==========================================================================");
    System.out.println("MONTE CARLO SIMULATION: SIMPLE TEST");
    System.out.println(
        "==========================================================================");
    System.out.println("| Higher Attr | Upgrades | Downgrades | Success Chance (%) |");
    System.out.println("|-------------|----------|------------|--------------------|");

    int[] higherAttrs = { 1, 2, 3, 4, 5, 6, 7 };
    int[] upgradesList = { 0, 1, 2, 3 };
    int[] downgradesList = { 0, 1, 2, 3 };

    for (int higher : higherAttrs) {
      for (int upgrades : upgradesList) {
        int successes = 0;
        for (int i = 0; i < ITERATIONS; i++) {
          AttributePair pair = new AttributePair();
          pair.setFirst(new Attribute("H", higher));
          pair.setSecond(new Attribute("L", 1));

          SimpleTest simpleTest = new SimpleTest(pair);
          if (upgrades > 0) {
            simpleTest.upgrade(upgrades);
          }
          simpleTest.roll();
          SimpleResult result = simpleTest.resolve();
          if (result.resultCategory() == ResultCategory.SUCCESS) {
            successes++;
          }
        }
        double successChance = (double) successes / ITERATIONS * 100.0;
        System.out.printf("| %11d | %8d | %10d | %17.2f%% |\n", higher, upgrades, 0,
            successChance);
      }
      for (int downgrades : downgradesList) {
        int successes = 0;
        for (int i = 0; i < ITERATIONS; i++) {
          AttributePair pair = new AttributePair();
          pair.setFirst(new Attribute("H", higher));
          pair.setSecond(new Attribute("L", 1));

          SimpleTest simpleTest = new SimpleTest(pair);
          if (downgrades > 0) {
            simpleTest.downgrade(downgrades);
          }
          simpleTest.roll();
          SimpleResult result = simpleTest.resolve();
          if (result.resultCategory() == ResultCategory.SUCCESS) {
            successes++;
          }
        }
        double successChance = (double) successes / ITERATIONS * 100.0;
        System.out.printf("| %11d | %8d | %10d | %17.2f%% |\n", higher, 0, downgrades,
            successChance);
      }
    }
    System.out.println(
        "==========================================================================\n");
  }

  @Test
  void runSuccessTestSimulation() {
    System.out.println(
        "==========================================================================");
    System.out.println("MONTE CARLO SIMULATION: SUCCESS TEST");
    System.out.println(
        "==========================================================================");
    System.out.println("| Lower Attr | Upgrades | Downgrades | Avg Success Points |");
    System.out.println("|------------|----------|------------|--------------------|");

    int[] lowerAttrs = { 1, 2, 3, 4, 5, 6, 7 };
    int[] upgradesList = { 0, 1, 2, 3 };
    int[] downgradesList = { 0, 1, 2, 3 };

    for (int lower : lowerAttrs) {
      for (int upgrades : upgradesList) {
        double totalPoints = 0;
        for (int i = 0; i < ITERATIONS; i++) {
          AttributePair pair = new AttributePair();
          pair.setFirst(new Attribute("H", 8));
          pair.setSecond(new Attribute("L", lower));

          SuccessTest successTest = new SuccessTest(pair);
          if (upgrades > 0) {
            successTest.upgrade(upgrades);
          }
          successTest.roll();
          SuccessResult result = successTest.resolve();
          totalPoints += result.successPoints();
        }
        double avgPoints = totalPoints / ITERATIONS;
        System.out.printf("| %10d | %8d | %10d | %18.2f |\n", lower, upgrades, 0,
            avgPoints);
      }
      for (int downgrades : downgradesList) {
        double totalPoints = 0;
        for (int i = 0; i < ITERATIONS; i++) {
          AttributePair pair = new AttributePair();
          pair.setFirst(new Attribute("H", 8));
          pair.setSecond(new Attribute("L", lower));

          SuccessTest successTest = new SuccessTest(pair);
          if (downgrades > 0) {
            successTest.downgrade(downgrades);
          }
          successTest.roll();
          SuccessResult result = successTest.resolve();
          totalPoints += result.successPoints();
        }
        double avgPoints = totalPoints / ITERATIONS;
        System.out.printf("| %10d | %8d | %10d | %18.2f |\n", lower, 0, downgrades,
            avgPoints);
      }
    }
    System.out.println(
        "==========================================================================\n");
  }

  @Test
  void runComplexTestSimulation() {
    System.out.println(
        "====================================================================================================");
    System.out.println("MONTE CARLO SIMULATION: COMPLEX TEST");
    System.out.println(
        "====================================================================================================");
    System.out.println(
        "| Higher Attr | Lower Attr | Upgrades | Downgrades | Success Chance (%) | Avg Success Pts (Overall) |");
    System.out.println(
        "|-------------|------------|----------|------------|--------------------|---------------------------|");

    int[][] attrPairs = {
        { 2, 1 },
        { 3, 2 },
        { 4, 3 },
        { 5, 4 }
    };
    int[] upgradesList = { 0, 1, 2, 3 };
    int[] downgradesList = { 0, 1, 2, 3 };

    for (int[] attrs : attrPairs) {
      int higher = attrs[0];
      int lower = attrs[1];
      for (int upgrades : upgradesList) {
        int successes = 0;
        double totalPoints = 0;
        for (int i = 0; i < ITERATIONS; i++) {
          AttributePair pair = new AttributePair();
          pair.setFirst(new Attribute("H", higher));
          pair.setSecond(new Attribute("L", lower));

          ComplexTest complexTest = new ComplexTest(pair);

          complexTest.roll();
          SimpleResult progress = complexTest.progress();
          if (progress.resultCategory() == ResultCategory.SUCCESS) {
            complexTest.roll();
            successes++;
          }
          ComplexResult result = complexTest.resolve();
          totalPoints += result.successPoints();
        }
        double successChance = (double) successes / ITERATIONS * 100.0;
        double avgPoints = totalPoints / ITERATIONS;
        System.out.printf("| %11d | %10d | %8d | %10d | %17.2f%% | %25.2f |\n",
            higher, lower, upgrades, 0, successChance, avgPoints);
      }
      for (int downgrades : downgradesList) {
        int successes = 0;
        double totalPoints = 0;
        for (int i = 0; i < ITERATIONS; i++) {
          AttributePair pair = new AttributePair();
          pair.setFirst(new Attribute("H", higher));
          pair.setSecond(new Attribute("L", lower));

          ComplexTest complexTest = new ComplexTest(pair);
          if (downgrades > 0) {
            complexTest.downgrade(downgrades);
          }

          complexTest.roll();
          SimpleResult progress = complexTest.progress();
          if (progress.resultCategory() == ResultCategory.SUCCESS) {
            complexTest.roll();
            successes++;
          }
          ComplexResult result = complexTest.resolve();
          totalPoints += result.successPoints();
        }
        double successChance = (double) successes / ITERATIONS * 100.0;
        double avgPoints = totalPoints / ITERATIONS;
        System.out.printf("| %11d | %10d | %8d | %10d | %17.2f%% | %25.2f |\n",
            higher, lower, 0, downgrades, successChance, avgPoints);
      }
    }
    System.out.println(
        "====================================================================================================\n");
  }
}

