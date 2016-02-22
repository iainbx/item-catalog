"""
SQLAlchemy database model for the web app.
"""
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


# Web site user model
class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    email = Column(String(250), nullable = False, unique=True)
    picture = Column(String(250))
    

# Category model
class Category(Base):
    __tablename__ = 'category'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)
    items = relationship("Item", cascade="all,delete", backref="category")    

    @property
    def serialize(self):
        return {
            'id'        : self.id,
            'name'      : self.name,
            'user_id'   : self.user_id,
            'items'     : [i.serialize for i in self.items]
        }


# Item model
class Item(Base):
    __tablename__ = 'item'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    description = Column(String(1000))
    pub_date = Column(DateTime)
    image = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'name'          : self.name,
            'description'   : self.description,
            'id'            : self.id,
            'user_id'       : self.user_id,
            'category_id'   : self.category_id,
            'image'         : self.image,
            'pub_date'      : self.pub_date
       }

