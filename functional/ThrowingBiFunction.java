package com.tidalsoft.service.kubernetes.webclient.client.global;

import java.util.function.BiFunction;

/**
 * @author Eugene Pankov
 * on 09/12/2020
 */
@SuppressWarnings("PMD")
@FunctionalInterface
public interface ThrowingBiFunction<T, U, R, E extends Exception> {
    R apply(T var1, U var2) throws E;

    static <T, U, R> BiFunction<T, U, R> wrapper(final ThrowingBiFunction<T, U, R, Exception> throwingBiFunction) {
        return (arg1, arg2) -> {
            try {
                return throwingBiFunction.apply(arg1, arg2);
            } catch (final Exception ex) {
                throw new RuntimeException(ex);
            }
        };
    }
}
