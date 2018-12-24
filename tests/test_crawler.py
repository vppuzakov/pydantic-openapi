from doc.examples.photo import Photo
from doc.examples.user import User
from src.models.crawler import Crawler


def test_photo() -> None:
    openapi = Crawler.crawl(Photo)
    assert openapi.dto.title == "Photo"
    assert openapi.path == "doc.examples.photo"
    assert len(openapi.properties) == 2


def test_user() -> None:
    openapi = Crawler.crawl(User)
    assert openapi.dto.title == "User"
    assert openapi.path == "doc.examples.user"
    for prop in openapi.properties:
        if prop.title == 'photo':
            assert prop.model.path == "doc.examples.photo"
    assert len(openapi.properties) == 4
