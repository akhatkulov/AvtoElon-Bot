from sqlalchemy import create_engine, MetaData, Table, Column, Integer,VARCHAR, String, BigInteger, func
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
    cid = Column(BigInteger, unique=True)
    name = Column(VARCHAR(100))
    year = Column(VARCHAR(25), default="0")
    is_clear = Column(VARCHAR(25),default="0")
    color = Column(VARCHAR(25), default="0")
    oil =  Column(VARCHAR(100),default="benzin")
    cost = Column(VARCHAR(100),default="$")
    phone = Column(VARCHAR(100),default="+998")
    location = Column(VARCHAR(100),default="samarqand")

class Channels(Base):
    __tablename__ = 'channels_avtosalon'
    id = Column(Integer, primary_key=True, autoincrement=True)
    link = Column(String, default="None", unique=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

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
        session.add(user)
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