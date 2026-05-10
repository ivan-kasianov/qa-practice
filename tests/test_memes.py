import pytest

from data.data import (
    NEGATIVE_PAYLOAD,
    INVALID_IDS,
    INVALID_URLS,
    NEGATIVE_PAYLOAD_FOR_UPDATE_MEME
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
    "negative_payload, "
    "expected_status_code",
    NEGATIVE_PAYLOAD
)
def test_post_meme_with_negative_payload(
    create_meme_endpoint,
    negative_payload,
    expected_status_code
):
    create_meme_endpoint.create_new_meme(negative_payload)
    create_meme_endpoint.check_response_status_code(expected_status_code)


def test_get_one_meme(
    get_one_meme_endpoint,
    get_meme_id,
    payload_for_get_meme
):
    get_one_meme_endpoint.get_one_meme(get_meme_id)
    get_one_meme_endpoint.check_response_status_code(200)
    get_one_meme_endpoint.check_response_meme_id_is_correct(get_meme_id)
    get_one_meme_endpoint.check_response_text_is_correct(
        payload_for_get_meme["text"]
    )
    get_one_meme_endpoint.check_response_url_is_correct(
        payload_for_get_meme["url"]
    )
    get_one_meme_endpoint.check_response_tags_is_correct(
        payload_for_get_meme["tags"]
    )
    get_one_meme_endpoint.check_response_colors_is_correct(
        payload_for_get_meme["info"]["colors"]
    )
    get_one_meme_endpoint.check_response_objects_is_correct(
        payload_for_get_meme["info"]["objects"]
    )


@pytest.mark.parametrize(
    "invalid_meme_id, "
    "expected_status_code",
    INVALID_IDS
)
def test_get_not_exist_meme(
    get_one_meme_endpoint,
    invalid_meme_id,
    expected_status_code
):
    get_one_meme_endpoint.get_one_meme(invalid_meme_id)
    get_one_meme_endpoint.check_response_status_code(expected_status_code)


def test_get_memes(get_all_memes_endpoint):
    get_all_memes_endpoint.get_memes()
    get_all_memes_endpoint.check_response_status_code(200)
    get_all_memes_endpoint.check_response_quantity_memes_is_correct()


@pytest.mark.parametrize("wrong_urls, expected_status_code", INVALID_URLS)
def test_get_memes_with_wrong_url(
    get_all_memes_endpoint,
    wrong_urls,
    expected_status_code
):
    get_all_memes_endpoint.get_memes_with_wrong_url(wrong_urls)
    get_all_memes_endpoint.check_response_status_code(expected_status_code)


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
    "negative_payload_for_update, "
    "expected_status_code",
    NEGATIVE_PAYLOAD_FOR_UPDATE_MEME
)
def test_update_meme_with_negative_payload(
    update_meme_endpoint,
    negative_payload_for_update,
    expected_status_code,
    get_meme_id
):
    update_meme_endpoint.update_meme(
        negative_payload_for_update,
        get_meme_id
    )
    update_meme_endpoint.check_response_status_code(expected_status_code)


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
    "invalid_meme_id, "
    "expected_status_code",
    INVALID_IDS)
def test_delete_meme_with_invalid_id(
    delete_meme_endpoint,
    invalid_meme_id,
    expected_status_code
):
    delete_meme_endpoint.delete_meme(
        invalid_meme_id
    )
    delete_meme_endpoint.check_response_status_code(
        expected_status_code
    )
