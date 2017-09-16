from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from base import *


class User(Base):

    def __init__(self, name, image):
        self.name = name
        self.image = image

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    image = Column(Text)
