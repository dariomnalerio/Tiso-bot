import io
import aiohttp
import discord
import uuid
from api.random_image import GetRandomUrl


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
