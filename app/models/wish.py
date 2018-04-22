from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship


class Wish(Base):
    id = Column(Integer,primary_key=True)
    user = relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15),nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean,default=False)