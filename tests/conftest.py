import pytest
import os
from dotenv import load_dotenv


from endpoints.authorize import Authorize
from endpoints.create_meme import CreateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.get_meme import GetMeme
from endpoints.get_memes import GetMemes
from endpoints.update_meme import UpdateMeme
from endpoints.endpoint import Endpoint

load_dotenv()


@pytest.fixture
def payload():
    return {
        "text": "pepe_hacker",
        "url": "https://img.artpal.com/746703/1-24-3-11-6-12-29m.jpg",
        "tags": ["hacker", "qa"],
        "info": {
            "colors": ["green", "black", "pink"],
            "objects": ["computer", "frog"]
        }
    }


@pytest.fixture
def payload_for_update_meme(get_meme_id):
    return {
        "id": get_meme_id,
        "text": "pepe_hacker_UPD",
        "url": "https://img.artpal.com/746703/1-24-3-11-6-12-29m.jpg",
        "tags": ["hacker_UPD", "qa_UPD"],
        "info": {
            "colors": ["green", "black", "pink"],
            "objects": ["computer", "frog"]
        }
    }


@pytest.fixture
def payload_for_get_meme():
    return {
        "text": "breaking_bad",
        "url": ("https://cdn-ilbehnh.nitrocdn.com/"
                "AOxksxAhcKtFnVREtJHVDtOdxvrNXqFw/"
                "assets/images/optimized/rev-5702753/blog.domotz.com/"
                "wp-content/uploads/2023/12/juniour.jpg"
                ),
        "tags": ["documentation", "it"],
        "info": {
            "colors": ["brown", "black", "white"],
            "objects": ["Walter White", "Team Lead", "Junior"]
        }
    }


@pytest.fixture(scope="session")
def auth_endpoint():
    return Authorize()


@pytest.fixture(scope="session")
def auth_token(auth_endpoint):
    user = os.getenv("AUTH_NAME")
    user_payload = {"name": user}
    token = auth_endpoint.get_token_from_file()
    if token is None:
        token = auth_endpoint.authorize_and_write_token_to_file(user_payload)
    return token


@pytest.fixture
def create_meme_endpoint(auth_token):
    return CreateMeme(token=auth_token)


@pytest.fixture
def get_one_meme_endpoint(auth_token):
    return GetMeme(token=auth_token)


@pytest.fixture
def get_meme_id(
    create_meme_endpoint,
    payload_for_get_meme,
    delete_meme_endpoint
):
    create_meme_endpoint.create_new_meme(payload_for_get_meme)
    meme_id = create_meme_endpoint.returned_meme_id()
    yield meme_id
    delete_meme_endpoint.delete_meme(meme_id)


@pytest.fixture
def delete_meme_endpoint(auth_token):
    return DeleteMeme(token=auth_token)


@pytest.fixture
def get_all_memes_endpoint(auth_token):
    return GetMemes(token=auth_token)


@pytest.fixture
def update_meme_endpoint(auth_token):
    return UpdateMeme(token=auth_token)


@pytest.fixture
def base_endpoint():
    return Endpoint(token=None)
