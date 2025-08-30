package org.pcsiszar.corsair.dice;

public class TestDie extends Die {
    private int nextRoll;

    public TestDie(long sides) {
        super(sides);
    }

    public void setNextRoll(int nextRoll) {
        this.nextRoll = nextRoll;
    }

    @Override
    public int roll() {
        this.value = nextRoll;
        return nextRoll;
    }
}
