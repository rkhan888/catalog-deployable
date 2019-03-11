from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from catalogModels import Category, Item, Base, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

user_rows_deleted = session.query(User).delete()
print(user_rows_deleted)

data = session.query(Category).all()
item = session.query(Item).all()
user = session.query(User).all()

for u in user:
    print(u.id)
    print(u.name)

#for d in data:
#    print(d.id)
#    print(d.name)

#for i in item:
#    print(i.id)
#    print(i.name)
#    print(i.description)
#    print(i.cat_name)

