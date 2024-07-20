from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.engine.url import URL
from app.db.base import Base
from app.core.config import settings

#Db Engine
def create_database():
    
    #SqlAlchemy URL object for better URL handling
    database_url = URL.create(
        settings.db_url,
        username=settings.db_username,
        password=settings.db_pwd,
        host=settings.db_host,
        port=settings.db_port,
        database=settings.db_name
    )
    
    #connecting to db server
    engine = create_engine(database_url)
    conn = engine.connect()
    conn.execute("commit")
    try:
        #try to create the new database if it doesn't exist
        conn.execute(f"CREATE DATABASE {settings.db_name}")
    except ProgrammingError as e:
        print(f"Databas already exists: {e}")
    finally:
        conn.close()
    
#To initialize db
def init_db():
    
    #Create database if doesn't exist
    create_database()
    
    #Connection to the given database
    specific_database_url = URL.create(
        settings.db_url, 
        username=settings.db_username, 
        password=settings.db_pwd, 
        host=settings.db_host, 
        port=settings.db_port,
        database=settings.db_name
    )
    specific_engine = create_engine(specific_database_url)
    Base.metadata.create_all(bind=specific_engine)
    
    #Create SessionFactory configuration  to be used by the engine
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=specific_engine)
    
    from app.api.models.user import User
    
    return SessionLocal