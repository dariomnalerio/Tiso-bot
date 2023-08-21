def GetRandomUrl():
    """Get random image url from the database"""
    from database.database import get_session
    from sqlalchemy.sql import func
    from models.random_image_model import RandomImage

    session = get_session()
    random_url = session.query(RandomImage.url).order_by(func.random()).first()
    session.close()
    return random_url
