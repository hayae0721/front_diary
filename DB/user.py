from DB.info import DATABASES

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# orm 과의 매핑 선언
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    idx = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(String(50))
    pw = Column(String(50))
    name = Column(String(50))

    def __init__(self, id, pw, name):
        self.id = id
        self.pw = pw
        self.name = name

    def __repr__(self):
        return f"User({self.id} {self.pw} {self.name})"


if __name__ == '__main__':
    Base.metadata.create_all(DATABASES)

    # 세션 연결
    Session = sessionmaker()
    Session.configure(bind=DATABASES)
    session = Session()

    test = User('test2', 'test1234', 'test_name2')

    # 세션에 추가
    session.add(test)
    session.commit()