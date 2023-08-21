import io
import aiohttp
import discord
import uuid
from api.random_image import GetRandomUrl


def GetRandomUrl():
    """Get random image url from the database"""
    from database.database import get_session
    from sqlalchemy.sql import func
    from models.random_image_model import RandomImage

    session = get_session()
    random_url = session.query(RandomImage.url).order_by(func.random()).first()
    session.close()
    return random_url


def randomImage(bot):
    @bot.command()
    async def randomImage(ctx):
        """Send a message with a random image"""
        random_url = GetRandomUrl()

        # Asynchronously fetch the image
        async with aiohttp.ClientSession() as session:
            async with session.get(random_url[0]) as res:
                if res.status == 200:
                    # Read image bytes
                    image_bytes = await res.read()

                    # Generate random filename
                    image_uuid = uuid.uuid4()
                    image_filename = f"ri-{image_uuid}.png"

                    # Create a discord.File from the image bytes
                    image_file = discord.File(io.BytesIO(
                        image_bytes), filename=image_filename)

                    # Send the image to the Discord channel
                    await ctx.send(file=image_file)
                else:
                    await ctx.send("Error getting image")
