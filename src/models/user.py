from sqlalchemy import Column, Integer, String, Boolean, DateTime, BigInteger
from sqlalchemy.dialects.sqlite import JSON
from datetime import datetime
from src.core.database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(
        BigInteger, 
        primary_key=True, 
        index=True, 
        comment="Telegram user ID"
    )
    is_bot = Column(
        Boolean, 
        default=False, 
        comment="Is this a bot"
    )
    first_name = Column(
        String(255), 
        nullable=True, 
        comment="First name"
    )
    last_name = Column(
        String(255), 
        nullable=True, 
        comment="Last name"
    )
    username = Column(
        String(255), 
        nullable=True, 
        index=True, 
        comment="Telegram username"
    )
    phone_number = Column(
        String(21), 
        nullable=True, 
        index=True, 
        comment="Phone number"
    )
    language_code = Column(
        String(10),
        nullable=True,
        comment="User language"
    )
    is_premium = Column(
        Boolean,
        default=False,
        comment="Is Telegram Premium user"
    )

    raw_data = Column(
        JSON,
        nullable=True, comment="Raw user data from Telegram"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        comment="Created at"
    )
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        comment="Update at"
    )

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, first_name={self.first_name})>"

    @property
    def full_name(self):
        names = [self.first_name, self.last_name]
        return " ".join(filter(None, names)) or self.username or str(self.id)
