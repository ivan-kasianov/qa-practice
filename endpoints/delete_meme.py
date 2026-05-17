
import allure
import requests

from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):

    def delete_meme(self, meme_id):
        self.response = requests.delete(
            f"{self.url}/{meme_id}",
            headers=self.headers
        )
        self.response_text = self.response.text
        return self.response

    @allure.step("Check the response code")
    def check_delete_message_is_correct(self, meme_id):
        expected_message = f"Meme with id {meme_id} successfully deleted"
        assert self.response_text == expected_message
