from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# PLACEHOLDER: Please ensure you replace the password with your actual PostgreSQL password
# Format: postgresql://<username>:<password>@<host>/<database_name>
SQLALCHEMY_PROD_DATABASE_URL = "postgresql://shareapp:hello123@localhost:5432/shareinfo"

# MySQL Connection String Format: 
# mysql+pymysql://<username>:<password>@<host>:<port>/<database_name>
SQLALCHEMY_QA_DATABASE_URL = "mysql+pymysql://shareapp_qauser:hello123@localhost:3306/shareinfo_qa"

qa_engine = create_engine(SQLALCHEMY_QA_DATABASE_URL)
qa_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=qa_engine)

prod_engine = create_engine(SQLALCHEMY_PROD_DATABASE_URL)
prod_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=prod_engine)


Base = declarative_base()

def get_qa_db():
    db = qa_SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_prod_db():
    db = prod_SessionLocal()
    try:
        yield db
    finally:
        db.close()
