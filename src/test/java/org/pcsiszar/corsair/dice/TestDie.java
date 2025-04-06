package org.pcsiszar.corsair.dice;

public class TestDie extends Die {
  private int fixedValue = 1;

  public static TestDie d6(int value) {
    return new TestDie(6, value);
  }

  public static TestDie d8(int value) {
    return new TestDie(8, value);
  }

  public static TestDie d10(int value) {
    return new TestDie(10, value);
  }

  public static TestDie d12(int value) {
    return new TestDie(12, value);
  }

  public static TestDie d20(int value) {
    return new TestDie(20, value);
  }

  public TestDie(long sides, int value) {
    super(sides);
    this.fixedValue = value;
  }

  @Override
  public int roll() {
    return fixedValue;
  }

  @Override
  public int getValue() {
    return fixedValue;
  }

  public void setFixedValue(int fixedValue) {
    this.fixedValue = fixedValue;
  }
}
