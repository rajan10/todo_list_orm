from models import User

from sqlalchemy import select
from sqlalchemy.orm import Session


# CRUD
class UserRepository:
    def get_all(self, session: Session) -> list[User]:
        stmt = select(User)
        result = session.scalars(stmt).all()
        return result

    def get_by_id(self, session: Session, id: int) -> User:
        stmt = select(User).filter(User.id == id)
        result = session.execute(stmt).scalar_one_or_none()
        return result

    def create(self, session: Session, user: User) -> None:
        session.add(user)
        session.commit()

    def create_many(self, session: Session, users: list[User]) -> None:
        session.add_all(users)
        session.commit()
