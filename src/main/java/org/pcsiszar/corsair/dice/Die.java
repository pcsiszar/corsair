package org.pcsiszar.corsair.dice;

import java.util.function.Supplier;

public class Die implements Comparable<Die> {
  private final Supplier<Double> randomGenerator;
  private final long sides;
  private boolean rolled = false;
  private int value = 1;

  public static Die d6() {
    return new Die(6);
  }

  public static Die d8() {
    return new Die(8);
  }

  public static Die d10() {
    return new Die(10);
  }

  public static Die d12() {
    return new Die(12);
  }

  public static Die d20() {
    return new Die(20);
  }

  public Die(long sides, Supplier<Double> randomGenerator) {
    this.sides = sides;
    this.randomGenerator = randomGenerator;
  }

  public Die(long sides) {
    this(sides, Math::random);
  }

  public int roll() {
    this.rolled = true;
    this.value = (int) Math.round(0.5 + randomGenerator.get() * this.sides);
    return this.value;
  }

  public int getValue() {
    return value;
  }

  public long getSides() {
    return sides;
  }

  public boolean isRolled() {
    return rolled;
  }

  @Override
  public int compareTo(Die o) {
    return Long.compare(this.value, o.value);
  }
}
