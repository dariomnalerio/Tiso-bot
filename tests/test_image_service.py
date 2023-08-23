"""
Test image service functions.
"""
import discord
import pytest
import asyncio
from services.image_service import fetch_image, process_image, is_valid_image_url

valid_image_url = "https://res.cloudinary.com/dhkyj5k4o/image/upload/v1689556365/learnaba/download_1_jtm44l.png"
invalid_image_url = "https://invalid-url.com/image.png"
invalid_url = "res.cloudinary.com/dhkyj5k4o/image/upload/v1689556365/learnaba/download_1_jtm44l.png"
non_image_url = "https://google.com"

# Fetch Image Tests


@pytest.mark.asyncio
async def test_fetch_valid_image():
    """
    Test valid image fetching with `fetch_image` function.

    Expected Output:
        The image data should not be None.
        The image data should be an instance of bytes.
    """

    image_data = await fetch_image(valid_image_url)

    assert image_data is not None
    assert isinstance(image_data, bytes)


@pytest.mark.asyncio
async def test_fetch_invalid_image():
    """
    Test invalid image fetching with `fetch_image` function.

    Expected Output:
        The image data should be None.
    """
    image_data = await fetch_image(invalid_image_url)

    assert image_data is None


@pytest.mark.asyncio
async def test_fetch_invalid_url():
    """
    Test invalid URL fetching with `fetch_image` function.

    Expected Output:
        The image data should be None.
    """
    url = "res.cloudinary.com/dhkyj5k4o/image/upload/v1689556365/learnaba/download_1_jtm44l.png"
    image_data = await fetch_image(invalid_url)

    assert image_data is None


@pytest.mark.asyncio
async def test_fetch_non_image_url():
    """
    Test non-image URL fetching with `fetch_image` function.

    Expected Output:
        The image data should be None.
    """
    image_data = await fetch_image(non_image_url)

    assert image_data is None


@pytest.mark.asyncio
async def test_fetch_timeout():
    """
    Test image fetching timeout with `fetch_image` function.

    Expected Output:
        TimeoutError.
    """
    async def delayed_fetch_image(valid_image_url):
        await asyncio.sleep(2)
        return await fetch_image(valid_image_url)

    with pytest.raises(TimeoutError):
        await asyncio.wait_for(delayed_fetch_image(valid_image_url), timeout=1)


# Process Image Tests

def test_process_valid_image():
    """
    Test valid image processing with `process_image` function.

    Expected Output:
        The image file should not be None.
        The image file should be an instance of discord.File.
    """
    image_data = asyncio.run(fetch_image(valid_image_url))
    image_file = process_image(image_data)

    assert image_file is not None
    assert isinstance(image_file, discord.File)


def test_process_empty_image():
    """
    Test empty image processing with `process_image` function.

    Expected Output:
        The image file should be None.
    """
    image_data = b""
    image_file = process_image(image_data)

    assert image_file is None


def test_process_invalid_image_type():
    """
    Test invalid image type processing with `process_image` function.

    Expected Output:
        The image file should be None.
    """
    image_data = "invalid_image_data"
    image_file = process_image(image_data)

    assert image_file is None


def test_process_large_image():
    """
    Test large image processing with `process_image` function.

    Expected Output:
        The image file should be None.
    """
    image_data = b"0" * 1024 * 1024 * 8  # 8 MB
    image_file = process_image(image_data)

    assert image_file is not None
    assert isinstance(image_file, discord.File)


# Is Valid Image URL Tests


@pytest.mark.parametrize("url, expected_result", [
    (valid_image_url, True),
    (invalid_image_url, False),
    (non_image_url, False),
])
def test_is_valid_image_url(url, expected_result):
    result = is_valid_image_url(url)
    assert result == expected_result
