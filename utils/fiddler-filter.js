function OnBeforeResponse(oSession) {
    var host = oSession.hostname.ToLower();
    var method = oSession.oRequest.headers.HTTPMethod;

    // 🌿 Clio Traffic
    if (host.Contains("clio.com") || host.Contains("app.clio.com")) {
        if (oSession.PathAndQuery.Contains("/oauth/token")) {
            oSession["ui-color"] = "green";
            oSession["ui-comments"] = "Clio OAuth Token Exchange";
        } else if (method == "POST") {
            oSession["ui-color"] = "purple";
            oSession["ui-comments"] = "Clio ➝ POST Request";
        } else {
            oSession["ui-color"] = "green";
            oSession["ui-comments"] = "Clio Traffic";
        }
    }

        // 💻 QuickBooks Online Traffic
    else if (host.Contains("intuit.com") || host.Contains("quickbooks.intuit.com")) {
        if (oSession.PathAndQuery.Contains("/oauth2/v1/tokens")) {
            oSession["ui-color"] = "orange";
            oSession["ui-comments"] = "QBO OAuth Token Exchange";
        } else if (method == "POST") {
            oSession["ui-color"] = "purple";
            oSession["ui-comments"] = "QBO ➝ POST Request";
        } else {
            oSession["ui-color"] = "blue";
            oSession["ui-comments"] = "QuickBooks Traffic";
        }
    }

    // 🛠 Highlight PUT/PATCH operations
    if (method == "PUT" || method == "PATCH") {
        oSession["ui-color"] = "yellow";
        oSession["ui-comments"] = "Update Request: " + method;
    }

    // ❌ Highlight HTTP errors
    if (oSession.responseCode >= 400) {
        oSession["ui-color"] = "red";
        oSession["ui-comments"] = "HTTP Error " + oSession.responseCode;
    }

    // 👻 Optionally hide 304s
    if (m_Hide304s && oSession.responseCode == 304) {
        oSession["ui-hide"] = "true";
    }
}

