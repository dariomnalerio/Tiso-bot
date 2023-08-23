""""
    Module for image-related services.
"""
import aiohttp
import discord
import io
import uuid
import requests
from PIL import Image


async def fetch_image(url):
    """
    Fetches an image from the given URL using aiohttp.

    Args:
        url (str): The URL of the image to fetch.

    Returns:
        bytes: The raw image data, or None if fetching failed\n
        or the URL does not point to an image\n
        or the URL does not start with http:// or https://.
    """

    if not is_valid_image_url(url):
        return None

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                image_data = await response.read()
                return image_data
            else:
                return None


def process_image(image_data):
    """
    Processes the image data and creates a discord.File object.

    Args:
        image_data (bytes): The raw image data to process.

    Returns:
        discord.File or None: The processed image file, or None if processing failed.
    """
    if image_data and isinstance(image_data, bytes):
        image_uuid = uuid.uuid4()
        image_filename = f"ri-{image_uuid}.png"
        image_file = discord.File(io.BytesIO(
            image_data), filename=image_filename)
        return image_file
    else:
        return None


def is_valid_image_url(url):
    """
    Checks if the given URL points to a valid image.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL points to a valid image, False otherwise.
    """

    if not url.startswith("http://") and not url.startswith("https://"):
        return False  # Invalid URL format

    response = requests.get(url)

    if response.status_code != 200:
        return False

    content_type = response.headers.get('content-type')
    if not content_type or 'image' not in content_type:
        return False

    try:
        Image.open(io.BytesIO(response.content))
    except Exception as e:
        return False

    return True
