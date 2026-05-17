import os
from dotenv import load_dotenv

load_dotenv()

VALID_AUTH_PAYLOAD = {
    "name": os.getenv("AUTH_NAME")
}

INVALID_AUTH_PAYLOAD = [
    {
        "name": 123
    },
    {
        "name": 1.2
    },
    {
        "name": None
    },
    {
        "name": []
    },
    {
        "name": {}
    },
    {
        "name": ()
    }
]

INVALID_AUTH_TOKEN = [
    "text_token",
    9999999999,
    0,
    -1,
    2.3,
    None
]

NEGATIVE_PAYLOAD = [
    {
        "text": 123,  # Отправляем int вместо str
        "url": "https://img.artpal.com/746703/1-24-3-11-6-12-29m.jpg",
        "tags": ["hacker", "qa"],
        "info": {
            "colors": ["green", "black", "pink"],
            "objects": ["computer", "frog"]}
    },
    {
        "text": "123",
        "url": [123, 456],  # Отправляем list вместо str
        "tags": ["hacker", "qa"],
        "info": {
            "colors": ["green", "black", "pink"],
            "objects": ["computer", "frog"]}
    },
    {
        "text": "123",
        "url": "123",
        "tags": "hacker",  # Отправляем str вместо list
        "info": {
            "colors": ["green", "black", "pink"],
            "objects": ["computer", "frog"]}
    },
    {
        "text": "123",
        "url": "123",
        "tags": ["hacker", "qa"],
        "info": 123  # Отправляем int вместо dict
    },
    {}
]

NEGATIVE_PAYLOAD_FOR_UPDATE_MEME = [
    {
        "id": None,
        "text": "123",
        "url": "https://img.artpal.com/746703/1-24-3-11-6-12-29m.jpg",
        "tags": ["hacker", "qa"],
        "info": {
            "colors": ["green", "black", "pink"],
            "objects": ["computer", "frog"]}
    },
    {
        "id": "text",  # Отправляем str вместо int
        "text": "123",
        "url": "https://img.artpal.com/746703/1-24-3-11-6-12-29m.jpg",
        "tags": ["hacker", "qa"],
        "info": {
            "colors": ["green", "black", "pink"],
            "objects": ["computer", "frog"]}
    },
    {
        "id": ["test", "id"],  # Отправляем list вместо int
        "text": "123",
        "url": "123",
        "tags": ["hacker", "qa"],  # Отправляем str вместо list
        "info": {
            "colors": ["green", "black", "pink"],
            "objects": ["computer", "frog"]}
    },
    {
        "id": 0,
        "text": "123",
        "url": "123",
        "tags": ["hacker", "qa"],
        "info": 123  # Отправляем int вместо dict
    },
    {}
]

INVALID_IDS = [
    "text_id",
    9999999999,
    0,
    -1,
    2.3,
    " "
]

INVALID_URLS = [
    "memes",
    "memes",
    "meme/",
    "MEME",
    "random_page"
]

DATA_FOR_UNAUTHORIZED_REQUEST = [
    ("GET", "meme", None),
    ("GET", "meme/100", None),
    ("POST", "meme", {
        "text": "123",
        "url": "https://img.artpal.com/746703/1-24-3-11-6-12-29m.jpg",
        "tags": ["hacker", "qa"],
        "info": {
            "colors": ["green", "black", "pink"],
            "objects": ["computer", "frog"]}
    }
    ),
    ("PUT", "meme/100", {
        "text": "123",
        "url": "https://img.artpal.com/746703/1-24-3-11-6-12-29m.jpg",
        "tags": ["hacker", "qa"],
        "info": {
            "colors": ["green", "black", "pink"],
            "objects": ["computer", "frog"]}
    }
    ),
    ("DELETE", "meme/100", None)
]
