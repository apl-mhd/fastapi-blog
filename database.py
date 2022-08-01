from click import echo
from sqlalchemy import create_engine



engine = create_engine('sqlite:/// ./blog.db', echo=True)
