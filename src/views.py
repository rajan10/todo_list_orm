from sqlalchemy.orm import Session
from repository import UserRepository

from database import engine


user_repo = UserRepository()
# with Session(engine) as session:
#     result = user_repo.get_all(session=session)
#     print(result)

# with Session(engine) as session:
#     sita = User(name="sita", password="sita!", status=False)
#     user_repo.create(session=session, user=sita)

# with Session(engine) as session:
#     gita = User(name="gita", password="gita!", status=False)
#     mahesh = User(name="mahesh", password="mahesh!", status=True)
#     users = [gita, mahesh]
#     user_repo.create_many(session=session, users=users)

with Session(engine) as session:
    result = user_repo.get_by_id(session=session, id=19)
    print(result)
