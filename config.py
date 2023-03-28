from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import logging
from core.models import Base

# the rest of the code here



DATABASE_URL = 'sqlite:///database.db'
DB_ECHO = False
DB_AUTOCOMMIT = True
 
 
def get_engine(uri):
   logging.info('Connecting to database..')
   options = {
       'echo': DB_ECHO,
       'execution_options': {
           'autocommit': DB_AUTOCOMMIT
       }
   }
   return create_engine(uri, **options)
 

db_session = scoped_session(sessionmaker())
engine = get_engine(DATABASE_URL)

def init_session():
    db_session.configure(bind=engine)
    Base.metadata.create_all(engine)