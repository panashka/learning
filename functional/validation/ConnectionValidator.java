package com.tidalsoft.service.servicenow.webclient.client.validation;

import com.google.gwt.regexp.shared.RegExp;
import com.tidalsoft.service.servicenow.webclient.client.datatypes.ServiceNowConnection;
import com.tidalsoft.service.servicenow.webclient.client.global.Constants;

import static com.tidalsoft.service.servicenow.webclient.client.ServiceNowAdapter.UI_CONST;

/**
 * Created by eugene
 * on 6.02.20
 */
public class ConnectionValidator {
    private static final RegExp API_URL_REGEX = RegExp.compile("^(https?):\\/\\/[-a-zA-Z0-9+&@#\\/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#\\/%=~_|]$");
    private static final String BLANK_USER = "0";
    private static final int URL_LENGTH_LIMIT = 1000;
    private final Validator<ServiceNowConnection> connectionValidator;

    public ConnectionValidator() {
        connectionValidator = new Validator<>();
        connectionValidator
                .addCheck(this::checkApiUrlIsNotBlank, UI_CONST.i18nBlankUrlWarning())
                .addCheck(this::checkApiUrlPattern, UI_CONST.i18nUrlPatternWarning())
                .addCheck(this::checkApiUrlLength, UI_CONST.i18nInputLimitWarning())
                .addCheck(this::checkUser, UI_CONST.i18nNotExistingFieldWarning().replace("%", "User"));
    }

    public void validateConnection(final ServiceNowConnection connection) throws ValidationException {
        connectionValidator.validate(connection);
        if (connection.auth.getString().equals(Constants.Authentication.OAUTH2.name())) {
            oAuth2ConnectionValidator.validate(connection);
        }
    }

    private boolean checkApiUrlLength(final ServiceNowConnection connection) {
        return connection.apiUrl.getString().length() <= URL_LENGTH_LIMIT;
    }

    private boolean checkApiUrlIsNotBlank(final ServiceNowConnection connection) {
        return !connection.apiUrl.getString().isEmpty();
    }

    private boolean checkApiUrlPattern(final ServiceNowConnection connection) {
        return API_URL_REGEX.exec(connection.apiUrl.getString()) != null;
    }

    private boolean checkUser(final ServiceNowConnection connection) {
        final String userId = connection.userid.getString();
        return !userId.isEmpty() && !BLANK_USER.equals(userId);
    }
}
