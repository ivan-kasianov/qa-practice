NEGATIVE_PAYLOAD = [
    (
        {
            "text": 123,  # Отправляем int вместо str
            "url": "https://img.artpal.com/746703/1-24-3-11-6-12-29m.jpg",
            "tags": ["hacker", "qa"],
            "info": {
                "colors": ["green", "black", "pink"],
                "objects": ["computer", "frog"]}
        }, 400),
    (
        {
            "text": "123",
            "url": [123, 456],  # Отправляем list вместо str
            "tags": ["hacker", "qa"],
            "info": {
                "colors": ["green", "black", "pink"],
                "objects": ["computer", "frog"]}
        }, 400),
    (
        {
            "text": "123",
            "url": "123",
            "tags": "hacker",  # Отправляем str вместо list
            "info": {
                "colors": ["green", "black", "pink"],
                "objects": ["computer", "frog"]}
        }, 400),
    (
        {
            "text": "123",
            "url": "123",
            "tags": ["hacker", "qa"],
            "info": 123  # Отправляем int вместо dict
        }, 400),
    ({}, 400),
    (None, 500)
]

NEGATIVE_PAYLOAD_FOR_UPDATE_MEME = [
    (
        {
            "id": None,
            "text": "123",
            "url": "https://img.artpal.com/746703/1-24-3-11-6-12-29m.jpg",
            "tags": ["hacker", "qa"],
            "info": {
                "colors": ["green", "black", "pink"],
                "objects": ["computer", "frog"]}
        }, 400),
    (
        {
            "id": "text",  # Отправляем str вместо int
            "text": "123",
            "url": "https://img.artpal.com/746703/1-24-3-11-6-12-29m.jpg",
            "tags": ["hacker", "qa"],
            "info": {
                "colors": ["green", "black", "pink"],
                "objects": ["computer", "frog"]}
        }, 400),
    (
        {
            "id": ["test", "id"],  # Отправляем list вместо int
            "text": "123",
            "url": "123",
            "tags": ["hacker", "qa"],  # Отправляем str вместо list
            "info": {
                "colors": ["green", "black", "pink"],
                "objects": ["computer", "frog"]}
        }, 400),
    (
        {
            "id": 0,
            "text": "123",
            "url": "123",
            "tags": ["hacker", "qa"],
            "info": 123  # Отправляем int вместо dict
        }, 400),
    ({}, 400),
    (None, 500)
]

INVALID_IDS = [
    ("text_id", 404),
    (9999999999, 404),
    (0, 404),
    (-1, 404),
    (2.3, 404),
    (" ", 404)
]

INVALID_URLS = [
    ("memes", 404),
    ("meme/", 404),
    ("MEME", 404),
    ("random_page", 404)
]
