package com.tidalsoft.service.kubernetes.webclient.client.global;

/**
 * @author Eugene Pankov
 * on 09/12/2020
 */
@SuppressWarnings("PMD")
@FunctionalInterface
public interface Throwing4Function<A, B, C, D, F, E extends Exception> {
    F apply(A var1, B var2, C var3, D var4) throws E;

    static <A, B, C, D, F> Function4<A, B, C, D, F> wrapper(final Throwing4Function<A, B, C, D, F, Exception> function) {
        return (var1, var2, var3, var4) -> {
            try {
                return function.apply(var1, var2, var3, var4);
            } catch (final Exception ex) {
                throw new RuntimeException(ex);
            }
        };
    }
}
