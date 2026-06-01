from sqlalchemy import Column, Integer, String, Boolean, DateTime, BigInteger, ForeignKey, Text
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from src.core.database import Base


class Chat(Base):
    
    __tablename__ = "chats"
    
    id = Column(BigInteger, primary_key=True, index=True, comment="Telegram chat ID")
    type = Column(String(50), nullable=False, comment="Chat type: private, group, supersgroup, channel")
    title = Column(String(255), nullable=True, comment="Chat title (for groups/channels)")
    username = Column(String(255), nullable=True, index=True, comment="Chat username")
    description = Column(Text, nullable=True, comment="Chat description")
    
    is_bot = Column(Boolean, default=False, comment="Is bot contact")
    phone_number = Column(String(20), nullable=True, index=True, comment="Phone number")
    is_premium = Column(Boolean, default=False, comment="Is Telegram Premium user")
    
    is_pinned = Column(Boolean, default=False, comment="Pinned chat")
    is_archived = Column(Boolean, default=False, comment="Archived chat")
    is_muted = Column(Boolean, default=False, comment="Muted chat")
    is_read = Column(Boolean, default=True, comment="All messages read")
    
    unread_count = Column(Integer, default=0, comment="Unread messages count")
    last_message_id = Column(BigInteger, nullable=True, comment="Last message ID")
    
    raw_data = Column(JSON, nullable=True, comment="Raw chat data from Telegram")
    
    created_at = Column(DateTime, default=datetime.utcnow, comment="Created at")
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment="Updated at")
    last_message_date = Column(DateTime, nullable=True, comment="Last message date")
    
    # Relationships
    # messages = relationship("Message", back_populates="chat", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Chat(id={self.id}, title={self.title or self.username}, type={self.type})>"
    
    @property
    def display_name(self):
        return self.title or self.username or self.first_name or str(self.id)
