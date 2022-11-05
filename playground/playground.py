from sqlalchemy import create_engine
from app import app

playground = create_engine(app.config.get('PLAYGROUND_DATABASE_URI'))
