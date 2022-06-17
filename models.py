from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text, true
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP, String
from database import Base


class post(Base):
    __tablename__ = "rfid"

    id = Column(Integer, primary_key=True, nullable=False)
    serialno = Column(String, nullable=False)
    create_at = Column(TIMESTAMP(timezone=true), nullable=False, server_default=text('now()'))


class user(Base):
    __tablename__ = "Employee"

    id = Column(Integer, primary_key= True, nullable=False)
    name = Column(String, nullable=False)
    Employeeid = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    serialno = Column(String, nullable=False)
    profileimg = Column(String, nullable=False)
    details = Column(String, nullable=False)
    create_at = Column(TIMESTAMP(timezone=true), nullable=False, server_default=text('now()'))
