import time


class AccessToken(object):
    # The number of seconds before the token expires, when
    # we will already try to refresh it
    TOKEN_BUFFER = 10

    def __init__(self, client):
        self._access_token = None
        self._expires_at = 0
        self.client = client

    # PROTECTED

    # The bearer token that can be used directly in API request headers
    def bearer_token(self):
        return "Bearer {0}".format(self._token())

    # PRIVATE

    # Returns the access token if it is still valid,
    # or refreshes it if it is not (or about to expire)
    def _token(self):
        if self._needs_refresh():
            self._update_access_token()
        return self._access_token

    # Checks if the token needs a refesh by checking if the token
    # is nil or (about to) expire(d)
    def _needs_refresh(self):
        has_access_token = self._access_token is not None
        current_time_window = int(time.time()) + self.TOKEN_BUFFER
        has_valid_token = current_time_window < self._expires_at

        return not (has_access_token and has_valid_token)

    # Fetches a new access token and stores it and its expiry date
    def _update_access_token(self):
        response = self._fetch_access_token()
        self._store_access_token(response.result)

    # Fetches a new access token
    def _fetch_access_token(self):
        return self.client._unauthenticated_request(
            'POST',
            '/v1/security/oauth2/token',
            {
                'grant_type': 'client_credentials',
                'client_id': self.client.client_id,
                'client_secret': self.client.client_secret
            }
        )

    # Store an access token and calculates the expiry date
    def _store_access_token(self, data):
        self._access_token = data.get('access_token', None)
        current_time = int(time.time())
        self.expires_at = current_time + data.get('expires_in', 0)
