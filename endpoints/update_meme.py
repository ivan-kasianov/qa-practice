import requests

from endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):
    def __init__(self, token):
        super().__init__(token)
        self.url = f"{self.base_url}/meme"

    def update_meme(self, payload, meme_id):
        self.response = requests.put(
            f"{self.url}/{meme_id}",
            json=payload,
            headers=self.headers
        )
        try:
            self.response_json = self.response.json()
        except ValueError:
            self.response_json = {}
        return self.response
