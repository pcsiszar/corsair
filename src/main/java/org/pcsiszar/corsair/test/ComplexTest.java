package org.pcsiszar.corsair.test;

import org.pcsiszar.corsair.character.AttributePair;
import org.pcsiszar.corsair.dice.DicePool;
import org.pcsiszar.corsair.dice.Die;

import java.util.Comparator;
import java.util.List;
import java.util.function.Supplier;
import java.util.stream.Collectors;

import static org.pcsiszar.corsair.dice.DicePool.PoolState;

public class ComplexTest extends Test<ComplexResult> {

    private final AttributePair attributePair;
    private ComplexTestStage stage = ComplexTestStage.ACTION_STAGE;
    private SimpleResult actionResult;

    public ComplexTest(AttributePair attributePair) {
        super(DicePool.ofSize(attributePair.getHigher().getValue()));
        this.attributePair = attributePair;
    }

    public ComplexTest(AttributePair attributePair, Supplier<Die> dieSupplier) {
        super(DicePool.ofSize(attributePair.getHigher().getValue(), dieSupplier));
        this.attributePair = attributePair;
    }

    @Override
    public void upgrade(int n) {
        if (stage != ComplexTestStage.ACTION_STAGE) {
            throw new IllegalStateException("Upgrades have to be taken in the action stage.");
        }
        super.upgrade(n);
    }

    @Override
    public void downgrade(int n) {
        if (stage != ComplexTestStage.ACTION_STAGE) {
            throw new IllegalStateException("Downgrades have to be taken in the action stage.");
        }
        super.downgrade(n);
    }

    public void progress() {
        if (stage == ComplexTestStage.SUCCESS_STAGE) {
            throw new IllegalStateException("Already in success stage.");
        }
        if (dicePool.getState() == PoolState.RESOLVED) {
            throw new IllegalStateException("Already resolved.");
        }
        if (dicePool.getState() != PoolState.ROLLED) {
            throw new IllegalStateException("Roll dice before progressing.");
        }
        actionResult = SimpleTest.getSimpleResult(dicePool);
        if (actionResult.resultCategory() == ResultCategory.SUCCESS) {
            List<Die> diceForSuccess = dicePool.getDice().stream()
                    .sorted(Comparator.reverseOrder())
                    .limit(attributePair.getLower().getValue())
                    .collect(Collectors.toList());
            dicePool = new DicePool(diceForSuccess);
            stage = ComplexTestStage.SUCCESS_STAGE;
        } else {
            dicePool.resolve();
        }
    }

    @Override
    public ComplexResult evaluate() {
        if (actionResult.resultCategory() == ResultCategory.FAILURE) {
            return new ComplexResult(actionResult.resultCategory(), 0);
        }

        return new SuccessTest(dicePool).evaluate().toComplexResult();
    }

    enum ComplexTestStage {
        ACTION_STAGE,
        SUCCESS_STAGE
    }
}
