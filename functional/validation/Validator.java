package com.tidalsoft.service.servicenow.webclient.client.validation;

import com.tidalsoft.service.servicenow.webclient.client.util.Either;

import java.util.ArrayList;
import java.util.List;
import java.util.function.BinaryOperator;
import java.util.function.Function;
import java.util.function.Predicate;

import static com.tidalsoft.service.servicenow.webclient.client.util.Either.right;

/**
 * Created by eugene
 * on 6.02.20
 */
public class Validator<T> {

    private static final String DEFAULT_VALUE_IS_NULL_MESSAGE = "Validation value is null: ";

    private final String valueIsNull;

    private final List<Function<T, Either<String, T>>> validators = new ArrayList<>();

    public Validator(final String valueNullErrorMsg) {
        valueIsNull = valueNullErrorMsg;
    }

    public Validator() {
        valueIsNull = DEFAULT_VALUE_IS_NULL_MESSAGE;
    }

    public void validate(final T entity) throws ValidationException {
        if (entity == null) {
            throw new ValidationException(valueIsNull);
        }

        final Either<String, T> result = validators.stream().reduce(right(entity), Either::bind, combiner());
        if (result.isLeft()) {
            throw new ValidationException(result.leftValue());
        }
    }

    public Validator<T> addCheck(final Predicate<T> check, final String message) {
        validators.add(value -> check.test(value) ? right(value) : Either.left(message));
        return this;
    }

    public Validator<T> addCheck(final Function<T, Either<String, T>> validator) {
        validators.add(validator);
        return this;
    }

    private BinaryOperator<Either<String, T>> combiner() {
        return (either1, either2) -> either2.isLeft() ? either2 : either1;
    }
}
