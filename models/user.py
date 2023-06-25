from models.models import User, session

def add_user(email, password):
    new_user = User(email=email, password=password)
    session.add(new_user)
    session.commit()
    session.close()


def check_user(email):
    existing_user = session.query(User).filter_by(email=email).first()
    if not existing_user:
        return True
    else:
        return False