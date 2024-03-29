import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

load_dotenv()

# Create connection
engine = create_engine('postgresql://{}:{}@{}/{}'.format(
    os.getenv('PG_USER'), os.getenv('PG_PWD'), os.getenv('PG_HOST'), os.getenv('PG_DB')
))

# Create all not created defined tables
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
