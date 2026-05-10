import requests

from endpoints.endpoint import Endpoint


class GetMeme(Endpoint):
    def __init__(self, token):
        super().__init__(token)
        self.url = f"{self.base_url}/meme"

    def get_one_meme(self, meme_id):
        self.meme_id = meme_id
        self.response = requests.get(
            f"{self.url}/{meme_id}",
            headers=self.headers
        )
        try:
            self.response_json = self.response.json()
        except ValueError:
            self.response_json = {}
        return self.response
