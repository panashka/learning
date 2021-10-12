package com.tidalsoft.service.kubernetes.webclient.client.global;

import java.util.Objects;
import java.util.function.Function;

/**
 * Created by ekrylovich
 * on 13.6.17.
 */
@SuppressWarnings("PMD")
final class Left<E, A> extends Either<E, A> {

    private final E value;

    Left(final E value) {
        this.value = Objects.requireNonNull(value);
    }

    public <B> Either<E, B> map(final Function<A, B> f) {
        return new Left<>(value);
    }

    public <B> Either<E, B> bind(final Function<A, Either<E, B>> f) {
        return new Left<>(value);
    }

    public Either<E, A> orElse(final Function0<Either<E, A>> a) {
        return a.apply();
    }

    @Override
    public String toString() {
        return "Left(" + value + ")";
    }

    @Override
    public boolean isLeft() {
        return true;
    }

    @Override
    public boolean isRight() {
        return false;
    }

    @Override
    public E leftValue() {
        return this.value;
    }

    @Override
    public A rightValue() {
        throw new IllegalStateException("getRight called on Left");
    }
}