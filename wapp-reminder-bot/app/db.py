from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session
from sqlalchemy.schema import ForeignKey

from config import config_dict

postgres_conn_string = "postgresql+psycopg2://{username}:{password}@{host}/{db_name}".format(
    username=config_dict["service_config"].postgres_user,
    password=config_dict["service_config"].postgres_password,
    host=config_dict["service_config"].postgres_host,
    db_name=config_dict["service_config"].postgres_db
)
engine = create_engine(postgres_conn_string, echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    username = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)
    api_key = Column(String)

    @staticmethod
    def get_users():
        return Session(engine).query(User).all()

    @staticmethod
    def get_user_by_username(username):
        return Session(engine).query(User).filter_by(username=username).first()


class Message(Base):
    __tablename__ = 'message'

    message_id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)


class MessageSenderRegistry(Base):
    __tablename__ = 'message_sender_registry'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, ForeignKey('user.username', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    message_id = Column(Integer, ForeignKey('message.message_id', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    sending_time = Column(DateTime)
    is_sent = Column(Boolean)
    is_repeating = Column(Boolean)
    repeating_interval = Column(Integer)

    @staticmethod
    def get_registry_by_username(username):
        return Session(engine).query(MessageSenderRegistry, Message).filter_by(username=username).all()

    @staticmethod
    def update_table(data_to_update):
        session = Session(engine)
        result = session.query(MessageSenderRegistry).filter_by(id=data_to_update["id"])

        result.update(data_to_update)
        session.commit()


Base.metadata.create_all(engine)
