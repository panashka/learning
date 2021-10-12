package com.tidalsoft.service.kubernetes.webclient.client.global;

/**
 * @author Eugene Pankov
 * on 09/12/2020
 */
@SuppressWarnings("PMD")
@FunctionalInterface
public interface Throwing3Function<A, B, C, D, E extends Exception> {
    D apply(A var1, B var2, C var3) throws E;

    static <A, B, C, D> Function3<A, B, C, D> wrapper(final Throwing3Function<A, B, C, D, Exception> function) {
        return (var1, var2, var3) -> {
            try {
                return function.apply(var1, var2, var3);
            } catch (final Exception ex) {
                throw new RuntimeException(ex);
            }
        };
    }
}
