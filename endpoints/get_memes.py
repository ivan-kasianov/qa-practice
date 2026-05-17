import requests

from endpoints.endpoint import Endpoint


class GetMemes(Endpoint):

    def get_memes(self, url="meme"):
        self.response = requests.get(
            f"{self.base_url}/{url}",
            headers=self.headers
        )
        try:
            self.response_json = self.response.json()
        except ValueError:
            self.response_json = {}
        return self.response
