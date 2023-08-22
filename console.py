from api.random_image import AddUrl
import typer

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
            AddUrl(url)
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
    typer.echo(GetRandomUrl())


if __name__ == "__main__":
    app()
