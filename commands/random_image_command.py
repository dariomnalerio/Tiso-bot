from api.random_image import get_random_url
from services.image_service import fetch_image, process_image
from database.database import get_session


def randomImage(bot):
    @bot.command()
    async def randomImage(ctx):
        """Send a message with a random image"""
        # Get a random image URL
        session = get_session()
        random_url = get_random_url(session)

        # Fetch the image data asynchronously
        image_data = await fetch_image(random_url[0])

        # Process the image data and create a discord.File object
        image_file = process_image(image_data)

        if image_file:
            # Send the image to the Discord channel
            await ctx.send(file=image_file)
        else:
            # Handle the case when fetching or processing failed
            await ctx.send("Error getting image")
