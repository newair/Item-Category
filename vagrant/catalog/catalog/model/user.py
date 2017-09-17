from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from base import *


class User(Base):

    def __init__(self, id, name, image):
        self.id = id
        self.name = name
        self.image = image

    __tablename__ = 'user'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    image = Column(String)
