#
# secret.py: GCP secret manager utility functions
#

import google.auth
from google.cloud import secretmanager

CREDENTIALS, PROJECT_ID = google.auth.default()

client = secretmanager.SecretManagerServiceClient()


def get(secret_name):
    secret_name = client.secret_version_path(PROJECT_ID, secret_name, "latest")
    response = client.access_secret_version(request={"name": secret_name})
    return response.payload.data.decode("UTF-8")
