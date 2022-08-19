from sqlalchemy import Column, Integer, String, Text
from database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, index=True)
    name = Column(String, index=True)
    link = Column(String, index=True)
    label1= Column(String, index=True)
    label2 = Column(String, index=True)
    content = Column(Text, index=True)