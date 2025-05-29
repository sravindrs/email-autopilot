from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    google_id = Column(String, unique=True, nullable=False)
    access_token = Column(String, nullable=False)
    refresh_token = Column(String, nullable=False)
    token_expiry = Column(DateTime, nullable=False)

class EmailMeta(Base):
    __tablename__ = "emails_meta"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    message_id = Column(String, nullable=False)
    thread_id = Column(String, nullable=False)
    received_at = Column(DateTime, nullable=False)
    cluster_id = Column(Integer)
    urgency_score = Column(Float)
    workflow_executed = Column(Boolean, default=False)
    workflow_id = Column(Integer)