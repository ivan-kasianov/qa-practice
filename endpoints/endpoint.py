import allure
import requests


class Endpoint():

    base_url = "http://memesapi.course.qa-practice.com"

    def __init__(self, token):
        self.token = None
        self.response = None
        self.response_json = None
        self.url = f"{self.base_url}/meme"
        self.headers = {"Authorization": f"{token}"}

    @allure.step("Check status code")
    def check_response_status_code(self, expected_status_code):
        assert self.response.status_code == expected_status_code, (
            f"Status code is not {expected_status_code}. "
            f"But, status code is {self.response.status_code}"
        )

    @allure.step("Check that text is the same as sent")
    def check_response_text_is_correct(self, text):
        assert self.response_json["text"] == text

    @allure.step("Check that url is the same as sent")
    def check_response_url_is_correct(self, url):
        assert self.response_json["url"] == url

    @allure.step("Check that all memes have been received")
    def check_response_quantity_memes_is_correct(self):
        assert (
            len(self.response_json["data"]) > 0
        ), "The objects have not yet been created"

    @allure.step("Check that tags are the same as sent")
    def check_response_tags_is_correct(self, expected_tags):
        assert set(self.response_json["tags"]) == set(expected_tags)

    @allure.step("Check that colors are the same as sent")
    def check_response_colors_is_correct(self, expected_colors):
        assert (self.response_json["info"]["colors"]) == expected_colors

    @allure.step("Check that objects are the same as sent")
    def check_response_objects_is_correct(self, expected_objects):
        assert (self.response_json["info"]["objects"]) == expected_objects

    @allure.step("Check meme id is the same as sent")
    def check_response_meme_id_is_correct(self, meme_id):
        assert (
            str(self.response_json["id"]) == str(meme_id)
        ), "No meme exists with that id"

    def request_without_aut_token(self, method, url_path, payload):
        self.response = requests.request(
            method=method,
            url=f"{self.base_url}/{url_path}",
            json=payload,
        )
        return self.response
