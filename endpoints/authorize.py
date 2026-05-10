import requests

from endpoints.endpoint import Endpoint


class Authorize(Endpoint):

    def __init__(self, user=None):
        super().__init__(token=None)
        self.user = user

    def post_authorize(self, user):
        self.response = requests.post(
            f"{self.base_url}/authorize",
            json=user
        )
        self.response_json = self.response.json()
        return self.response_json["token"]

    def get_authorize(self, token):
        self.response = requests.get(
            f"{self.base_url}/authorize/{token}"
        )
        return self.response.status_code

    def get_token_from_file(self):
        with open(".token", "r") as file:
            token = file.read()
            if self.get_authorize(token) == 200:
                return token

    def write_token_to_file(self, user):
        token = self.post_authorize(user)
        with open(".token", "w") as file:
            file.write(token)
        return token
