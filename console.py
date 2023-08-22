from api.random_image import AddUrl
import typer
from database.database import get_session
from services.image_service import is_valid_image_url

app = typer.Typer()


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
            AddUrl(url, session)
            typer.echo("URL added successfully")
        except ValueError as e:
            typer.echo(str(e))


@app.command()
def get():
    """
    Get a random image URL from the random image table.

    This function fetches a random image URL from the random image table using SQLAlchemy.

    Returns:
        str: A random image URL.
    """
    from api.random_image import GetRandomUrl
    session = get_session()
    typer.echo(GetRandomUrl(session))


if __name__ == "__main__":
    app()
