from sqlalchemy.orm import Session
from app.api.models.user import User

def create_user(db: Session, user_data: dict):
    user = User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: str, update_data: dict):
    db.query(User).filter(User.id == user_id).update(update_data)
    db.commit()

def delete_user(db: Session, user_id: str):
    user = get_user(db, user_id)
    db.delete(user)
    db.commit()
    return {"ok": True}