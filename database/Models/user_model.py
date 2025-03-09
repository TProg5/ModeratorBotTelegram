from database.base_model import Base

from sqlalchemy import BigInteger, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_telegram: Mapped[int] =  mapped_column(BigInteger, nullable=True)

    warn = relationship("Warns", back_populates="user", uselist=False)
