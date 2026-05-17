import requests
import allure


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
        try:
            self.response_json = self.response.json()
        except ValueError:
            self.response_json = {}
        return self.response_json.get("token")

    def get_authorize(self, token):
        self.response = requests.get(
            f"{self.base_url}/authorize/{token}"
        )
        self.response_text = self.response.text
        return self.response.status_code

    def get_token_from_file(self):
        with open(".token", "r") as file:
            token = file.read()
            if self.get_authorize(token) == 200:
                return token

    def authorize_and_write_token_to_file(self, user):
        token = self.post_authorize(user)
        with open(".token", "w") as file:
            file.write(token)
        return token

    @allure.step("Check of the received token")
    def check_token_is_present(self):
        assert "token" in self.response_json, (
            "There is no token in the response"
        )
        assert self.response_json["token"] is not None, (
            "Token is empty"
        )
        assert isinstance(self.response_json["token"], str), (
            "Token is not a string"
        )

    @allure.step("Check token owner")
    def check_token_owner(self, user):
        assert self.response_text == f"Token is alive. Username is {user}"
