from db import Base, engine
from models import User, Reports

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")