from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://admin:123@localhost:5432/uni-db"
SQLALCHEMY_DATABASE_URL = "postgresql://root:YBfURfdyej4NgjOhVN1k0Q1Z@aaa:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)  #connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()