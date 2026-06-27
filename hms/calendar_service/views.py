import os

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

from google_auth_oauthlib.flow import Flow
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponse

SCOPES = [
    "https://www.googleapis.com/auth/calendar"
]

flow = Flow.from_client_secrets_file(
    "credentials.json",
    scopes=SCOPES,
    redirect_uri="http://localhost:8000/oauth2callback/"
)


def google_login(request):
    if not request.user.is_authenticated:
        return HttpResponse("Please log in to HMS first.")

    request.session["user_id"] = request.user.id

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        prompt="consent"
    )

    request.session["state"] = state

    return HttpResponseRedirect(authorization_url)

def oauth2callback(request):

    flow.fetch_token(
        authorization_response=request.build_absolute_uri()
    )

    credentials = flow.credentials

    User = get_user_model()

    user_id = request.session.get("user_id")

    if not user_id:
        return HttpResponse("User session not found.")

    user = User.objects.get(id=user_id)

    user.google_access_token = credentials.token
    user.google_refresh_token = credentials.refresh_token
    user.google_token_expiry = credentials.expiry

    user.save()

    return HttpResponse(
        "Google Calendar connected successfully!"
    )