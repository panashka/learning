package com.tidalsoft.stargate.tech;

import java.util.Objects;
import java.util.function.Function;

/**
 * Created by ekrylovich
 * on 18.6.18.
 */
public final class Pair<A, B> {
    private final A first;
    private final B second;

    private Pair(final A first, final B second) {
        this.first = Objects.requireNonNull(first);
        this.second = Objects.requireNonNull(second);
    }

//  MethodNameCheck:OFF
    @SuppressWarnings({"PMD.MethodNamingConventions", "PMD.ShortMethodName"})
    public A _1() {
        return first;
    }

    @SuppressWarnings({"PMD.MethodNamingConventions", "PMD.ShortMethodName"})
    public B _2() {
        return second;
    }
//  MethodNameCheck:ON

    @SuppressWarnings({"PMD.MethodNamingConventions", "PMD.ShortMethodName"})
    public static <T, V> Pair<T, V> of(final T first, final V second) {
        return new Pair<>(first, second);
    }

    /**
     * Map the first element of the product.
     *
     * @param function The function to map with.
     * @return A product with the given function applied.
     */
    public <C> Pair<C, B> map1(final Function<A, C> function) {
        return bimap(function, Function.identity());
    }

    /**
     * Map the second element of the product.
     *
     * @param function The function to map with.
     * @return A product with the given function applied.
     */
    public <C> Pair<A, C> map2(final Function<B, C> function) {
        return bimap(Function.identity(), function);
    }

    /**
     * Swaps this product-2 (pair)
     *
     * @return the swapped pair
     */
    public Pair<B, A> swap() {
        return of(_2(), _1());
    }

    /**
     * Split this product between two argument functions and combine their
     * output.
     *
     * @param function1 A function that will map the first element of this product.
     * @param function2 A function that will map the second element of this product.
     * @return A new product with the first function applied to the second
     * element and the second function applied to the second element.
     */
    public <C, D> Pair<C, D> bimap(final Function<A, C> function1, final Function<B, D> function2) {
        return of(function1.apply(_1()), function2.apply(_2()));
    }

    /**
     * Returns a first projection as a function. To be used with higher order
     * functions.
     *
     * @return function that will project the given Pair to the first component
     */
    public static <A, B> Function<Pair<A, B>, A> fst() {
        return Pair::_1;
    }

    /**
     * Returns a second projection as a function. To be used with higher order
     * functions.
     *
     * @return function that will project the given Pair to the second component
     */
    public static <A, B> Function<Pair<A, B>, B> snd() {
        return Pair::_2;
    }

    @Override
    public boolean equals(final Object object) {
        if (this == object) {
            return true;
        }
        if (object == null || getClass() != object.getClass()) {
            return false;
        }
        final Pair<?, ?> pair = (Pair<?, ?>) object;
        return Objects.equals(first, pair.first) &&
                Objects.equals(second, pair.second);
    }

    @Override
    public int hashCode() {
        return Objects.hash(first, second);
    }

    @Override
    public String toString() {
        return "(" + first + "," + second + ")";
    }
}
