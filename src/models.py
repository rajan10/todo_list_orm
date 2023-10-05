from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


from sqlalchemy.orm import Session
from database import engine, Base
from database import create_table


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(30))
    status: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return f"<User={self.id}:{self.name}>"


# create_table()

# with Session(engine) as session:
#     hari = User(name="hari", password="hari!", status=True)
#     ganesh = User(name="ganesh", password="ganesh!", status=True)
#     rita = User(name="rita", password="rita!", status=False)
#     gita = User(name="gita", password="gita!", status=False)

#     session.add_all([hari, ganesh, rita, gita])

#     session.commit()
