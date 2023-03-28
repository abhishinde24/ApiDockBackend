from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base, declared_attr

class BaseModel(object):
  @declared_attr
  def __tablename__(self):
        return self.__name__.lower()


  def to_dict(self):
      intersection = set(self.__table__.columns.keys()) & set(self.FIELDS)
      return dict(map(
          lambda key:
              (key,
                  (lambda value: self.FIELDS[key](value) if value else None)
                  (getattr(self, key))),
              intersection))


  FIELDS = {}

Base = declarative_base(cls=BaseModel)

class ApiDetail(Base):
  id = Column(String(200), primary_key=True)
  name = Column(String(200), primary_key=True)
  url = Column(String(100), nullable=True)
  method = Column(String(100), nullable=True)
  authenticationType = Column(String(100), nullable=True)
  headers = Column(String(400), nullable=True)
  query_parameters = Column(String(400), nullable=True)
  request_body = Column(String(400), nullable=True)
  response_body = Column(String(400), nullable=True)

  FIELDS = {
      'id': str,
      'name': str,
      'url': str,
      'method': str,
      'authenticationType': str,
      'headers': str,
      'query_parameters': str,
      'request_body': str,
      'response_body': str,
  }

  FIELDS.update(Base.FIELDS)