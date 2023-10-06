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

    def update_by_id(
        self, session: Session, name: str, password: str, status: bool, id: int
    ) -> None:
        result = self.get_by_id(session, id)
        result.name = name
        result.password = password
        result.status = status
        session.commit()

    def delete_by_id(self, session: Session, id: int) -> None:
        result = self.get_by_id(session, id)
        session.delete(result)
        session.commit()

    def get_count(self, session: Session) -> int:
        result = session.query(User).count()
        return result
