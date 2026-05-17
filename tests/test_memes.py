import pytest

from data.data import (
    NEGATIVE_PAYLOAD,
    INVALID_IDS,
    INVALID_URLS,
    NEGATIVE_PAYLOAD_FOR_UPDATE_MEME,
    DATA_FOR_UNAUTHORIZED_REQUEST,
    VALID_AUTH_PAYLOAD,
    INVALID_AUTH_PAYLOAD, INVALID_AUTH_TOKEN
)


def test_post_meme(create_meme_endpoint, payload):
    create_meme_endpoint.create_new_meme(payload)
    create_meme_endpoint.check_response_status_code(200)
    create_meme_endpoint.check_response_text_is_correct(payload["text"])
    create_meme_endpoint.check_response_url_is_correct(payload["url"])
    create_meme_endpoint.check_response_tags_is_correct(payload["tags"])
    create_meme_endpoint.check_response_colors_is_correct(
        payload["info"]["colors"]
    )
    create_meme_endpoint.check_response_objects_is_correct(
        payload["info"]["objects"]
    )
    create_meme_endpoint.check_response_contains_meme_id()


@pytest.mark.parametrize(
    "negative_payload",
    NEGATIVE_PAYLOAD
)
def test_post_meme_with_negative_payload(
    create_meme_endpoint,
    negative_payload
):
    create_meme_endpoint.create_new_meme(negative_payload)
    create_meme_endpoint.check_response_status_code(400)


def test_get_one_meme(
    get_one_meme_endpoint,
    get_meme_id,
    payload_for_get_meme
):
    get_one_meme_endpoint.get_one_meme(get_meme_id)
    get_one_meme_endpoint.check_response_status_code(200)
    get_one_meme_endpoint.check_response_meme_id_is_correct(get_meme_id)


@pytest.mark.parametrize(
    "invalid_meme_id",
    INVALID_IDS
)
def test_get_not_exist_meme(
    get_one_meme_endpoint,
    invalid_meme_id
):
    get_one_meme_endpoint.get_one_meme(invalid_meme_id)
    get_one_meme_endpoint.check_response_status_code(404)


def test_get_memes(get_all_memes_endpoint):
    get_all_memes_endpoint.get_memes()
    get_all_memes_endpoint.check_response_status_code(200)
    get_all_memes_endpoint.check_response_quantity_memes_is_correct()


@pytest.mark.parametrize("wrong_urls", INVALID_URLS)
def test_get_memes_with_wrong_url(
    get_all_memes_endpoint,
    wrong_urls
):
    get_all_memes_endpoint.get_memes(wrong_urls)
    get_all_memes_endpoint.check_response_status_code(404)


def test_update_meme(
    update_meme_endpoint,
    payload_for_update_meme,
    get_meme_id
):
    update_meme_endpoint.update_meme(
        payload_for_update_meme,
        get_meme_id
    )
    update_meme_endpoint.check_response_status_code(200)
    update_meme_endpoint.check_response_meme_id_is_correct(get_meme_id)
    update_meme_endpoint.check_response_text_is_correct(
        payload_for_update_meme["text"]
    )
    update_meme_endpoint.check_response_url_is_correct(
        payload_for_update_meme["url"]
    )
    update_meme_endpoint.check_response_tags_is_correct(
        payload_for_update_meme["tags"]
    )
    update_meme_endpoint.check_response_colors_is_correct(
        payload_for_update_meme["info"]["colors"]
    )
    update_meme_endpoint.check_response_objects_is_correct(
        payload_for_update_meme["info"]["objects"]
    )


@pytest.mark.parametrize(
    "negative_payload_for_update",
    NEGATIVE_PAYLOAD_FOR_UPDATE_MEME
)
def test_update_meme_with_negative_payload(
    update_meme_endpoint,
    negative_payload_for_update,
    get_meme_id
):
    update_meme_endpoint.update_meme(
        negative_payload_for_update,
        get_meme_id
    )
    update_meme_endpoint.check_response_status_code(400)


def test_delete_meme(
    delete_meme_endpoint,
    get_one_meme_endpoint,
    get_meme_id
):
    delete_meme_endpoint.delete_meme(get_meme_id)
    delete_meme_endpoint.check_response_status_code(200)
    delete_meme_endpoint.check_delete_message_is_correct(get_meme_id)
    get_one_meme_endpoint.get_one_meme(get_meme_id)
    get_one_meme_endpoint.check_response_status_code(404)


@pytest.mark.parametrize(
    "invalid_meme_id",
    INVALID_IDS
)
def test_delete_meme_with_invalid_id(
    delete_meme_endpoint,
    invalid_meme_id
):
    delete_meme_endpoint.delete_meme(
        invalid_meme_id
    )
    delete_meme_endpoint.check_response_status_code(404)


@pytest.mark.parametrize(
    "method, path_url, payload",
    DATA_FOR_UNAUTHORIZED_REQUEST
)
def test_endpoints_without_aut_token(
    base_endpoint,
    method,
    path_url,
    payload
):
    base_endpoint.request_without_aut_token(method, path_url, payload)
    base_endpoint.check_response_status_code(401)


def test_successful_auth(auth_endpoint):
    auth_endpoint.post_authorize(VALID_AUTH_PAYLOAD)
    auth_endpoint.check_response_status_code(200)
    auth_endpoint.check_token_is_present()


@pytest.mark.parametrize(
    "invalid_auth_payload",
    INVALID_AUTH_PAYLOAD
)
def test_auth_with_invalid_payload(auth_endpoint, invalid_auth_payload):
    auth_endpoint.post_authorize(invalid_auth_payload)
    auth_endpoint.check_response_status_code(400)


def test_successful_token_validation(auth_endpoint, auth_token):
    auth_endpoint.get_authorize(auth_token)
    auth_endpoint.check_response_status_code(200)
    auth_endpoint.check_token_owner(VALID_AUTH_PAYLOAD["name"])


@pytest.mark.parametrize(
    "invalid_auth_token",
    INVALID_AUTH_TOKEN
)
def test_unsuccessful_token_validation(auth_endpoint, invalid_auth_token):
    auth_endpoint.get_authorize(invalid_auth_token)
    auth_endpoint.check_response_status_code(404)
