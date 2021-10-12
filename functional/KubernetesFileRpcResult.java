package com.tidalsoft.service.kubernetes.webclient.client.global;

import com.tidalsoft.webclient.base.client.datatypes.ServiceRequestErrors;
import com.tidalsoft.webclient.base.client.logic.CallbackPayload;
import com.tidalsoft.webclient.base.client.utils.XmlTools;
import com.tidalsoft.webclient.basedb.client.datacontrols.TidalDBTextArea;
import com.tidalsoft.webclient.basedb.client.datatypes.DBStringField;
import com.tidalsoft.webclient.basedb.client.dialogs.MessageDialog;

import static com.tidalsoft.service.kubernetes.webclient.client.KubernetesAdapter.UI_CONST;
import static com.tidalsoft.service.kubernetes.webclient.client.global.Constants.XML_REQUEST_ERRORMSG;

public final class KubernetesFileRpcResult {

    private static final String TES_RESULT = "tes:result";
    private static final String TES_OK = "tes:ok";
    private static final String TES_MESSAGE = "tes:message";

    private KubernetesFileRpcResult() {
        throw new UnsupportedOperationException(this.getClass() + " could not be instantiated by constructor");
    }

    public static boolean isTESResult(final String xmlResult) {
        return xmlResult.contains("<" + TES_RESULT);
    }

    public static boolean isOK(final String xmlResult) {
        final String tesOK = getElementValue(xmlResult, TES_OK);
        return Boolean.parseBoolean(tesOK);
    }

    public static String getMessage(final String xmlResult) {
        return XmlTools.unescapeXml(getElementValue(xmlResult, TES_MESSAGE));
    }

    public static String getFirstLines(final String msg, final int lines) {
        final StringBuilder stringBuilder = new StringBuilder(msg);
        if (lines > 0) {
            stringBuilder.delete(0, msg.length());
            int start = 0;
            for (int i = 0; i < lines; i++) {
                int end = msg.indexOf('\r', start);
                if (end == -1) {
                    end = msg.indexOf('\n', start);
                }
                if (end == -1) {
                    end = msg.length();
                    stringBuilder.append(msg, start, end);
                    break;
                }
                stringBuilder.append(msg, start, end);
                start = end + 1;
            }
        }
        return stringBuilder.toString();
    }

    public static String getElementValue(final String xmlResult, final String tag) {
        int start = xmlResult.indexOf("<" + tag);
        if (start == -1) {
            return null;
        }
        start = xmlResult.indexOf(">", start) + 1;
        final int end = xmlResult.indexOf("</" + tag, start);
        if (end == -1) {
            return null;
        }

        return xmlResult.substring(start, end);
    }

    public static boolean hasError(final CallbackPayload callbackPayload) {
        final String topic = callbackPayload.getTopic();
        boolean hasError = false;
        final String caption;
        final String message;

        if (callbackPayload.getReturnStatus() != CallbackPayload.OK) {
            hasError = true;
            caption = UI_CONST.i18nServiceRequestError();
            message = UI_CONST.i18nServiceRequestFailed().replace("%1", topic);
            handleFailedServiceRequest(caption, message);
        } else {
            final Object returnItem = callbackPayload.getReturnItem(1);
            if (returnItem instanceof String) {
                final String xmlData = (String) returnItem;
                if (xmlData.startsWith("<errors>")) {
                    final ServiceRequestErrors errors = new ServiceRequestErrors();
                    errors.initDataFields();
                    errors.deserialize(true, xmlData, "");

                    hasError = true;
                    caption = UI_CONST.i18nServiceRequestError();
                    message = UI_CONST.i18nServiceRequestFailedWithError()
                            .replace("%1", topic)
                            .replace("%2", errors.error.getString(0));
                    handleFailedServiceRequest(caption, message);
                } else {
                    final String errormsg = getElementValue(xmlData, XML_REQUEST_ERRORMSG);
                    if (errormsg != null) {
                        hasError = true;
                        MessageDialog.MessageOkWithDetails(UI_CONST.i18nLoadFileError(), UI_CONST.i18nInvalidFile(), null, null, errormsg);
                    }
                }
            }
        }
        return hasError;
    }

    private static void handleFailedServiceRequest(final String caption, final String message) {
        final TidalDBTextArea textArea = new TidalDBTextArea(null, new DBStringField());
        textArea.setText(message);
        textArea.setReadOnly(true);
        textArea.setVisibleLines(10);
        textArea.setWidth("100%");
        textArea.setHeight("100%");

        final MessageDialog dialog = new MessageDialog(caption, textArea, true);
        dialog.setWidth("500px");
        dialog.setHeight("400px");
        dialog.showCentered();
    }

}
