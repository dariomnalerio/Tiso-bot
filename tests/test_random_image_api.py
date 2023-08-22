import pytest
from api.random_image import GetRandomUrl, AddUrl
from database.database import get_in_memory_db
from models.random_image_model import RandomImage

url = "https://res.cloudinary.com/dhkyj5k4o/image/upload/v1689556365/learnaba/download_1_jtm44l.png"

# Mocking the database URL for testing purposes


@pytest.fixture
def session():
    """
    Create tables in the in-memory database and create a session.
    """
    session = get_in_memory_db()

    yield session
    session.close()


def test_add_url(session):
    """
    Test that a URL can be added to the database.

    This test checks that a URL can be added to the database using the AddUrl
    function.

    Args:
        session (Session): A SQLAlchemy session object.

    """
    AddUrl(url, session)

    added_url = session.query(RandomImage).filter_by(url=url).first()
    assert added_url is not None
    assert added_url.url == url


def test_get_random_url(session):
    """
    Test that a random URL can be retrieved from the database.

    This test checks that a random URL can be retrieved from the database using
    the GetRandomUrl function.
    """

    urls = [
        "https://res.cloudinary.com/dhkyj5k4o/image/upload/v1690586358/Presentation-page/smart-aba-dashboard_zqcy8v.webp",
        "https://res.cloudinary.com/dhkyj5k4o/image/upload/v1690586633/Presentation-page/next-ecommerce_g9uciu.webp",
        "https://res.cloudinary.com/dhkyj5k4o/image/upload/v1691264248/Presentation-page/WindowsTerminal_714NcjJBuE_1_kzkvls.webp",
        "https://res.cloudinary.com/dhkyj5k4o/image/upload/v1689556365/learnaba/download_1_jtm44l.png",
    ]

    for url_item in urls:
        AddUrl(url_item, session)

    random_url = GetRandomUrl(session)
    assert random_url is not None
    print("Retrieved URL:", random_url[0])
    assert random_url[0] in urls
