from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class Poll(Base):
    """
    Define a model for storing poll data

    Attributes:
        id (int): The ID of the poll.
        question (str): The question of the poll.
        options (list): The options of the poll.
        votes (list): The votes of the poll.  
    """
    __tablename__ = 'polls'

    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    options = relationship("PollOption", back_populates="poll")
    votes = relationship("Vote", back_populates="poll")


class PollOption(Base):
    """
    Define a model for storing poll option data

    Attributes:
        id (int): The ID of the poll option.
        option_text (str): The text of the poll option.
        poll_id (int): The ID of the poll.
        poll (Poll): The poll of the poll option.
        votes (list): The votes of the poll option.
    """
    __tablename__ = 'poll_options'

    id = Column(Integer, primary_key=True)
    option_text = Column(String, nullable=False)
    poll_id = Column(Integer, ForeignKey('polls.id'))
    poll = relationship("Poll", back_populates="options")
    votes = relationship("Vote", back_populates="option")


class Vote(Base):
    """
    Define a model for storing vote data

    Attributes:
        id (int): The ID of the vote.
        user_id (int): The ID of the user.
        option_id (int): The ID of the poll option.
        option (PollOption): The poll option of the vote.
        poll_id (int): The ID of the poll.
        poll (Poll): The poll of the vote.
    """
    __tablename__ = 'votes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)  # This could be Discord user IDs
    option_id = Column(Integer, ForeignKey('poll_options.id'))
    option = relationship("PollOption", back_populates="votes")
    poll_id = Column(Integer, ForeignKey('polls.id'))
    poll = relationship("Poll", back_populates="votes")
