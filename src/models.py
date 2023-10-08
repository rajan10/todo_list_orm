from sqlalchemy import String, ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship


from sqlalchemy.orm import Session
from database import engine, Base
from database import create_table


class User(Base):
    __tablename__ = "user"  # class level attribute that specifies the database table name correspong to classname
    # id is expected to hold integer type
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(30))  # mapped to some kind of db
    status: Mapped[bool] = mapped_column(
        default=False
    )  # if no value is explicitly provided for this col, it will default to 'False'
    tasks: Mapped[list["Task"]] = relationship(back_populates="user1", cascade="all")
    # so tasks can access the attributes of second table;if user is deleted, all tasks will be deleted

    def __repr__(self) -> str:
        return f"<User={self.id}:{self.name}>"


class Task(Base):
    __tablename__ = "task"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    status: Mapped[bool] = mapped_column(default=False)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id")
    )  # in Task, 1 FK user_id is created that is pointing to first table's id column; this is the way to write FK
    user1: Mapped["User"] = relationship(
        back_populates="tasks"
    )  # which means from Task object you can point to first table

    # implies codingobj.user = u cand find the right user
    def __repr__(self) -> str:
        return f"<Task->{self.id}:{self.name}>"


# create_table()

# with Session(engine) as session:
#     hari = User(name="hari", password="hari!", status=True)
#     ganesh = User(name="ganesh", password="ganesh!", status=True)
#     rita = User(name="rita", password="rita!", status=False)
#     gita = User(name="gita", password="gita!", status=False)

#     session.add_all([hari, ganesh, rita, gita])

#     session.commit()
