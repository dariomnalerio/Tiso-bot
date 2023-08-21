import aiohttp
import discord
import io
import uuid


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

    if not url.startswith("http://") and not url.startswith("https://"):
        return None  # Invalid URL format

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                content_type = response.headers.get("content-type")
                if content_type and content_type.startswith("image/"):
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
