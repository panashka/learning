package com.tidalsoft.service.kubernetes.webclient.client.global;

/**
 * Created by ekrylovich
 * on 13.6.17.
 */
@FunctionalInterface
public interface Function0<R> {
    /**
     * Apply the body of this function.
     *
     * @return the result of function application.
     */
    R apply();

}