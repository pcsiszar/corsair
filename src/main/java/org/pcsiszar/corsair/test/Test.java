package org.pcsiszar.corsair.test;

import org.pcsiszar.corsair.character.AttributePair;
import org.pcsiszar.corsair.dice.DicePool;
import org.pcsiszar.corsair.dice.Die;

import java.util.List;

public abstract class Test<T> {

  protected AttributePair attributePair;
  protected DicePool dicePool;

  public Test(AttributePair attributePair) {
    this.attributePair = attributePair;
    this.dicePool = getInitialDicePool(attributePair);
  }

  protected abstract DicePool getInitialDicePool(AttributePair attributePair);

  public void upgrade(int n) {
    dicePool.upgrade(n);
  }

  public void downgrade(int n) {
    dicePool.downgrade(n);
  }

  public void roll() {
    dicePool.roll();
  }

  public List<Die> takeGambit(int n) {
    return dicePool.takeGambit(n);
  }

  public void addGambit(Die die) {
    dicePool.addGambit(die);
  }

  public void mitigate(int n) {
    dicePool.mitigate(n);
  }

  public T resolve() {
    dicePool.resolve();
    return evaluate();
  }

  public abstract T evaluate();
}
