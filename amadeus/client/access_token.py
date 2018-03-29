import time


class AccessToken(object):
    # The number of seconds before the token expires, when
    # we will already try to refresh it
    TOKEN_BUFFER = 10

    def __init__(self, client):
        self.access_token = None
        self.expires_at = 0
        self.client = client

    # PROTECTED

    # The bearer token that can be used directly in API request headers
    def _bearer_token(self):
        return 'Bearer {0}'.format(self.__token())

    # PRIVATE

    # Returns the access token if it is still valid,
    # or refreshes it if it is not (or about to expire)
    def __token(self):
        if self.__needs_refresh():
            self.__update_access_token()
        return self.access_token

    # Checks if the token needs a refesh by checking if the token
    # is nil or (about to) expire(d)
    def __needs_refresh(self):
        has_access_token = self.access_token is not None
        current_time_window = int(time.time()) + self.TOKEN_BUFFER
        has_valid_token = current_time_window < self.expires_at

        return not (has_access_token and has_valid_token)

    # Fetches a new access token and stores it and its expiry date
    def __update_access_token(self):
        response = self.__fetch_access_token()
        self.__store_access_token(response.result)

    # Fetches a new access token
    def __fetch_access_token(self):
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
    def __store_access_token(self, data):
        self.access_token = data.get('access_token', None)
        current_time = int(time.time())
        self.expires_at = current_time + data.get('expires_in', 0)
