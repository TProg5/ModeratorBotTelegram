from database.base_model import Base

from sqlalchemy import ForeignKey
from sqlalchemy import Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

class Warns(Base):
    __tablename__ = 'warns'

    id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    warns: Mapped[int] = mapped_column(Integer, default=0)
    muted: Mapped[bool] = mapped_column(Boolean, default=False)

    user = relationship("Users", back_populates="warn")