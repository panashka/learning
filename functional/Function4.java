package com.tidalsoft.service.kubernetes.webclient.client.global;

/**
 * @author Eugene Pankov
 * on 09/12/2020
 */
@FunctionalInterface
public interface Function4<A, B, C, D, F> {
    F apply(A var1, B var2, C var3, D var4);
}
