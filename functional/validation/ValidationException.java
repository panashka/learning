package com.tidalsoft.service.servicenow.webclient.client.validation;

/**
 * Created by eugene
 * on 6.02.20
 */
public class ValidationException extends Exception {
    private static final long serialVersionUID = 1000L;

    public ValidationException() {
    }

    public ValidationException(final String message) {
        super(message);
    }
}