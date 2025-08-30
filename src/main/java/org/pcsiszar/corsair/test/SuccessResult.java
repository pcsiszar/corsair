package org.pcsiszar.corsair.test;

public record SuccessResult(int successPoints) {
    public ComplexResult toComplexResult() {
        return new ComplexResult(ResultCategory.SUCCESS, successPoints);
    }
}