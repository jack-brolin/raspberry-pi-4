from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.config import config_dict

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

    @classmethod
    def get_users(cls):
        return cls.query.all()

    @classmethod
    def get_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()


class Message(Base):
    __tablename__ = 'message'

    message_id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)


class MessageSenderRegisty(Base):
    __tablename__ = 'message_sender_registry'

    username = Column(Column, primary_key=True)
    message_id = Column(Integer)
    sending_time = Column(Datetime)

    user = relationship("User", back_populates="users")
    message = relationship("Message", back_populates="messages")

    @classmethod
    def get_registry_by_username(cls, username):
        return cls.query.filter_by(username=username).all()


User.invoices = relationship("MessageSenderRegisty", order_by=User.username, back_populates="user")
Message.invoices = relationship("MessageSenderRegisty", order_by=Message.message_id, back_populates="message")

Base.metadata.create_all(engine)
