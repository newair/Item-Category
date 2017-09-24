from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from base import *


class Category(Base):

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey("user.id"))
    name = Column(String)
    items = relationship("Item", back_populates="category", cascade="all,delete")
