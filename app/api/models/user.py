from sqlalchemy import Column, String, Integer, Boolean, ARRAY
from sqlalchemy.dialects.postgresql import JSONB
from app.db.base import Base

class User(Base):
    __tablename__= 'users'
    
    id = Column(String, primary_key=True, index=True)
    display_name = Column(String, index=True)
    source_principal_name = Column(String, unique=True, index=True)
    target_principal_name = Column(String, unique=True, index=True)
    primary_smtp_address = Column(String, unique=True)
    is_licensed = Column(Boolean, default=False)
    to_migrate_workloads = Column(ARRAY(String))
    license_description = Column(ARRAY(String))
    source_regional_configuration = Column(JSONB)
    target_regional_configuration = Column(JSONB)
    total_mail_messages_to_migrate = Column(Integer)
    total_mail_messages_migrated = Column(Integer)
    mailbox_properties = Column(JSONB)
    mail_message_errors = Column(Integer)
    total_files_to_migrate = Column(Integer)
    total_files_migrated = Column(Integer)
    onedrive_properties = Column(JSONB)
    migration_tasks = Column(ARRAY(JSONB))
    migration_status = Column(String)
    last_error = Column(String)