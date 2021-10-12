package com.tidalsoft.service.kubernetes.webclient.client.global;

/**
 * @author Eugene Pankov
 * on 09/12/2020
 */
@FunctionalInterface
public interface Function3<A, B, C, D> {
    D apply(A var1, B var2, C var3);
}
