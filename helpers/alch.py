from sqlalchemy import create_engine, MetaData, Table, Column, Integer, VARCHAR, String, BigInteger, func, JSON
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("postgresql://postgres:1945@localhost/postgres")
Base = declarative_base()

class User(Base):
    __tablename__ = 'user_avtosalon'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cid = Column(BigInteger, unique=True)
    step = Column(String, default="0")

class Step(Base):
    __tablename__ = 'step_avtosalon'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pic = Column(String)
    cid = Column(BigInteger, unique=True)
    name = Column(VARCHAR(100))
    year = Column(VARCHAR(25), default="0")
    km = Column(VARCHAR(25), default="0")
    is_clear = Column(VARCHAR(25), default="0")
    color = Column(VARCHAR(25), default="0")
    oil =  Column(VARCHAR(100), default="benzin")
    cost = Column(VARCHAR(100), default="$")
    phone = Column(VARCHAR(100), default="+998")
    location = Column(VARCHAR(100), default="samarqand")

class Posts(Base):
    __tablename__ = 'posts_avtosalon'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(VARCHAR(100))
    pic = Column(String)
    info = Column(String)

class Channels(Base):
    __tablename__ = 'channels_avtosalon'
    id = Column(Integer, primary_key=True, autoincrement=True)
    link = Column(String, default="None", unique=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def create_post(uid, pic, info):
    session = Session()
    try:
        x = Posts(uid=str(uid), pic=pic, info=info)
        session.add(x)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

def get_post(uid):
    session = Session()
    try:
        x = session.query(Posts).filter_by(uid=str(uid)).first()
        res = {"uid": x.uid, "pic": x.pic, "info": x.info} if x else None
        return res
    finally:
        session.close()

def get_all_user():
    session = Session()
    try:
        x = session.query(User.cid).all()
        res = [i[0] for i in x]
        return res
    finally:
        session.close()

def user_count():
    session = Session()
    try:
        x = session.query(func.count(User.id)).first()
        return x[0]
    finally:
        session.close()

def create_user(cid):
    session = Session()
    try:
        user = User(cid=int(cid), step="0")
        step = Step(cid=int(cid), pic="0", name="0", year="0", is_clear="0", color="0", oil="0", cost="0", phone="0", location="0")
        session.add(user)
        session.add(step)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

def get_members():
    session = Session()
    try:
        x = session.query(User).where(User.cid >= 0).all()
        return x
    finally:
        session.close()

def get_step(cid):
    session = Session()
    try:
        x = session.query(User).filter_by(cid=cid).first()
        return x.step if x else None
    finally:
        session.close()

def put_step(cid, step):
    session = Session()
    try:
        x = session.query(User).filter_by(cid=cid).first()
        if x:
            x.step = str(step)
            session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

def change_info(cid: int, type_info: str, value: str):
    session = Session()
    try:
        x = session.query(Step).filter_by(cid=cid).first()
        if x:
            if type_info == "name":
                x.name = value
            elif type_info == "pic":
                x.pic = value
            elif type_info == "year":
                x.year = value
            elif type_info == "is_clear":
                x.is_clear = value
            elif type_info == "color":
                x.color = value
            elif type_info == "oil":
                x.oil = value
            elif type_info == "cost":
                x.cost = value
            elif type_info == "phone":
                x.phone = value
            elif type_info == "location":
                x.location = value
            elif type_info == "km":
                x.km = value
            session.commit()
            return True
        else:
            return False
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error: {e}")
        return False
    finally:
        session.close()

def get_info(cid: int):
    session = Session()
    try:
        x = session.query(Step).filter_by(cid=cid).first()
        res = {
            "name": x.name,
            "pic": x.pic,
            "year": x.year,
            "is_clear": x.is_clear,
            "color": x.color,
            "oil": x.oil,
            "cost": x.cost,
            "phone": x.phone,
            "location": x.location,
            "km": x.km
        } if x else None
        return res
    finally:
        session.close()
