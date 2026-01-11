from database import sync_engine,Base, session_factory
import models
from models import User

Base.metadata.create_all(bind = sync_engine)

with session_factory() as session:
    user = User(email = 'jonh@gmail.com')
    session.add(user)
    session.commit()
