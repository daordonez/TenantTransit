from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, JSON, Float
from sqlalchemy.orm import relationship
from db.base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    source_user_principal_name = Column(String, unique=True, index=True)
    target_user_principal_name = Column(String, unique=True, index=True)
    country = Column(String)
    license = Column(String)
    is_licensed = Column(Boolean)
    mail_job_id = Column(Integer, ForeignKey('jobs.id'))
    migration_job_timestamp = Column(DateTime)
    mail_migration_rate_hour = Column(Float)

    jobs = relationship("Job", back_populates="user")

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    type = Column(String)
    init_timestamp = Column(DateTime)
    end_timestamp = Column(DateTime)
    errors = Column(JSON)

    user = relationship("User", back_populates="jobs")
    task = relationship("Task", back_populates="jobs")

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    start_timestamp = Column(DateTime)
    end_timestamp = Column(DateTime)
    user_list = Column(JSON)  # This will store a list of user IDs
    job_list = Column(JSON)   # This will store a list of job IDs
    errors = Column(JSON)

    jobs = relationship("Job", back_populates="task")
