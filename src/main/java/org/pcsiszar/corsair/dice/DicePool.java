package org.pcsiszar.corsair.dice;

import lombok.Getter;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class DicePool {
  private List<Die> dicePool;
  @Getter
  private PoolState state = PoolState.ASSEMBLED;
  @Getter
  private GambitState gambit = GambitState.GAMBIT_AVAILABLE;

  public static DicePool from(Die... dice) {
    return new DicePool(Arrays.asList(dice));
  }

  public static DicePool ofSize(int size) {
    return new DicePool(
        IntStream.range(0, size)
            .mapToObj(i -> Die.d10())
            .collect(Collectors.toList()));
  }

  public DicePool(List<Die> dicePool) {
    if (dicePool == null || dicePool.isEmpty()) {
      throw new IllegalArgumentException("Cannot create an empty Dice Pool");
    }
    this.dicePool = dicePool;
  }

  public void upgrade(int n) {
    if (state != PoolState.ASSEMBLED) {
      throw new IllegalStateException("Upgrade can only be done before applying downgrades.");
    }
    int remainingUpgrades = n;
    remainingUpgrades = upgradeDiceInInitialPool(remainingUpgrades);
    upgradeRemaining(remainingUpgrades);
    state = PoolState.UPGRADED;
  }

  private int upgradeDiceInInitialPool(int remainingUpgrades) {
    for (Die die : dicePool) {
      if (die.upgrade()) {
        remainingUpgrades--;
      }
    }
    return remainingUpgrades;
  }

  private void upgradeRemaining(int n) {
    Die dieToAdd = null;
    for (int i = 0; i < n; i++) {
      if (dieToAdd == null) {
        dieToAdd = Die.d10();
        dicePool.add(dieToAdd);
      } else {
        dieToAdd.upgrade();
        dieToAdd = null;
      }
    }
  }

  public void downgrade(int n) {
    if (state != PoolState.ASSEMBLED || state != PoolState.UPGRADED) {
      throw new IllegalStateException("Downgrades has to happen before the roll.");
    }
    int remainingDowngrades = downgradeInitialPool(n);
    downgradeRemaining(remainingDowngrades);
    state = PoolState.DOWNGRADED;
  }

  private int downgradeInitialPool(int n) {
    int remainingDowngrades = n;
    for (Die die : dicePool) {
      if (remainingDowngrades > 0) {
        if (die.downgrade()) {
          remainingDowngrades--;
        }
      }
    }
    return remainingDowngrades;
  }

  private void downgradeRemaining(int remainingDowngrades) {
    while (remainingDowngrades > 0 && dicePool.size() > 1) {
      dicePool.removeLast();
      remainingDowngrades--;
    }
  }

  public List<Die> takeGambit(int n) {
    if (gambit == GambitState.GAMBIT_ADDED) {
      throw new IllegalStateException(
          "You cannot take Gambit dice to the pool if you have added Gambit dice from it.");
    }
    List<Die> gambit = new ArrayList<>();
    List<Die> keep = new ArrayList<>();
    for (Die die : dicePool) {
      if (die.getSides() == die.getValue() && n > 0) {
        n--;
        gambit.add(die);
      } else {
        keep.add(die);
      }
    }
    this.dicePool = keep;
    this.gambit = GambitState.GAMBIT_TAKEN;
    return gambit;
  }

  public void addGambit(Die die) {
    if (state == PoolState.RESOLVED) {
      throw new IllegalStateException("Can't add Gambit die to a resolved roll");
    }
    if (gambit == GambitState.GAMBIT_TAKEN) {
      throw new IllegalStateException(
          "You cannot add Gambit dice to the pool if you have taken Gambit dice from it.");
    }
    die.roll();
    dicePool.add(die);
    gambit = GambitState.GAMBIT_ADDED;
  }

  public void mitigate(int n) {
    if (state != PoolState.ROLLED) {
      throw new IllegalStateException("Mitigation must occur after rolling!");
    }
    Collections.sort(dicePool);
    for (int i = 0; i < n; i++) {
      dicePool.removeLast();
    }
    state = PoolState.MITIGATED;
  }

  public void roll() {
    if (EnumSet.of(PoolState.ROLLED, PoolState.MITIGATED, PoolState.RESOLVED)
        .contains(state)) {
      throw new IllegalStateException("Roll was already completed, create a new DicePool!");
    }
    dicePool.forEach(Die::roll);
    state = PoolState.ROLLED;
  }

  public DicePool resolve() {
    this.state = PoolState.RESOLVED;
    return this;
  }

  public List<Die> getDice() {
    return dicePool;
  }

  enum PoolState {
    ASSEMBLED,
    UPGRADED,
    DOWNGRADED,
    ROLLED,
    MITIGATED,
    RESOLVED
  }

  enum GambitState {
    GAMBIT_AVAILABLE,
    GAMBIT_ADDED,
    GAMBIT_TAKEN
  }
}
