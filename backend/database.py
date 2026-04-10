from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import logging
import os

logger = logging.getLogger(__name__)

# PLACEHOLDER: Please ensure you replace the password with your actual PostgreSQL password
# Format: postgresql://<username>:<password>@<host>/<database_name>
SQLALCHEMY_PROD_DATABASE_URL = "postgresql://shareapp:hello123@localhost:5432/shareinfo"

# MySQL Connection String Format: 
# mysql+pymysql://<username>:<password>@<host>:<port>/<database_name>
SQLALCHEMY_QA_DATABASE_URL = "mysql+pymysql://shareapp_qauser:hello123@localhost:3306/shareinfo_qa"

# Reads from environment, defaults to "qa" if not provided
DATABASE_ENVIRONMENT = os.environ.get("DATABASE_ENVIRONMENT", "qa")



qa_engine = create_engine(SQLALCHEMY_QA_DATABASE_URL)
qa_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=qa_engine)

prod_engine = create_engine(SQLALCHEMY_PROD_DATABASE_URL)
prod_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=prod_engine)


Base = declarative_base()


def get_db():
    if DATABASE_ENVIRONMENT == "prod":
        logger.info("Using Production Database")
        db = prod_SessionLocal()
    else:
        logger.info("Using QA Database")
        db = qa_SessionLocal()
    try:
        yield db
    finally:
        db.close()
