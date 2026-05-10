import requests
import allure

from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    def __init__(self, token):
        super().__init__(token)
        self.url = f"{self.base_url}/meme"

    @allure.step("Create new meme")
    def create_new_meme(self, payload):
        self.response = requests.post(
            f"{self.url}",
            json=payload,
            headers=self.headers
        )
        try:
            self.response_json = self.response.json()
        except ValueError:
            self.response_json = {}
        return self.response

    def returned_meme_id(self):
        return self.response_json["id"]

    @allure.step("Check that objects are the same as sent")
    def check_response_contains_meme_id(self):
        assert "id" in self.response_json, "There is no id in the response"
        assert self.response_json["id"] is not None, "Id is empty"
