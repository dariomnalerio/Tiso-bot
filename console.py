from api.afk_count import get_afk_count, add_to_afk_count
from api.random_image import add_url, get_random_url
from api.poll import create_poll
import typer
from database.database import get_session
from services.image_service import is_valid_image_url

app = typer.Typer()

# Random image commands


@app.command()
def add(url: str = typer.Argument(..., help="The URL of the image to add to the database.")):
    """
    Add a new image URL to the random image table.

    This function adds a new image URL to the random image table using SQLAlchemy.
    """
    if not is_valid_image_url(url):
        raise ValueError("Invalid image URL")
    else:
        try:
            session = get_session()
            add_url(url, session)
            typer.echo("URL added successfully")
        except ValueError as e:
            typer.echo(str(e))


@app.command()
def add_many(url_list: str = typer.Argument(..., help="A comma-separated list of image URLs to add to the database.")):
    """
    Add multiple image URLs to the random image table.

    This function adds multiple image URLs to the random image table.
    """
    url_list = url_list.split(",")
    for url in url_list:
        if not is_valid_image_url(url):
            raise ValueError("Invalid image URL")
        else:
            try:
                session = get_session()
                add_url(url, session)
                typer.echo("URL added successfully")
            except ValueError as e:
                typer.echo(str(e))


@app.command()
def get():
    """
    Get a random image URL from the random image table.

    This function fetches a random image URL from the random image table.

    Returns:
        str: A random image URL.
    """
    session = get_session()
    typer.echo(get_random_url(session))


# Poll commands


@app.command()
def poll_create(
    question: str = typer.Argument(...,
                                   help="A string representing a question"),
    options: str = typer.Argument(...,
                                  help="A comma-separated list of options")
):
    """
    Create a poll.

    This function creates a poll with a question and options and adds it to the database.
    """
    session = get_session()

    options_list = options.split(",")

    typer.echo(create_poll(session, question, options_list))

# Afk count commands


@app.command()
def afk_count_get(discord_id: str = typer.Argument(..., help="The discord ID of the user."), server_id: str = typer.Argument(..., help="The discord ID of the server.")):
    """
    Get the current AFK count for a user.

    This function gets the current AFK count for a user.
    """
    session = get_session()
    typer.echo(get_afk_count(session, discord_id, server_id))


@app.command()
def afk_count_add(discord_id: str = typer.Argument(..., help="The discord ID of the user."), server_id: str = typer.Argument(..., help="The discord ID of the server.")):
    """
    Add a user to the AFK count.

    This function adds a user to the AFK count.
    """
    session = get_session()
    add_to_afk_count(session, discord_id, server_id)


if __name__ == "__main__":
    app()
