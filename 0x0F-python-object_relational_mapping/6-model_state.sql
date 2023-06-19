from sqlalchemy import create_engine
from models import State

# Create the engine to connect to your MySQL server
engine = create_engine('mysql://username:password@localhost:3306/database')

# Import all classes that inherit from Base

# Call create_all() to create the tables
Base.metadata.create_all(engine)
