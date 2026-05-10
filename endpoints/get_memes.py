import requests

from endpoints.endpoint import Endpoint


class GetMemes(Endpoint):
    def __init__(self, token):
        super().__init__(token)
        self.url = f"{self.base_url}/meme"

    def get_memes(self):
        self.response = requests.get(
            f"{self.url}",
            headers=self.headers
        )
        self.response_json = self.response.json()
        return self.response

    def get_memes_with_wrong_url(self, wrong_url):
        self.response = requests.get(
            f"{self.base_url}/{wrong_url}",
            headers=self.headers
        )
        try:
            self.response_json = self.response.json()
        except ValueError:
            self.response_json = {}
        return self.response
