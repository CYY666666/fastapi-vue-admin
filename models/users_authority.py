from models.base import Base
from sqlalchemy import Column, BigInteger, String, DateTime, Boolean
from datetime import datetime
from utils.snow_flake import generate_id


class Menus(Base):
    __tablename__ = "sys_user_authority"
    __table_args__ = ({"comment": "用户权限"})
    id = Column(BigInteger, primary_key=True, index=True)
    sys_user_id = Column(BigInteger, comment="用户ID")
    sys_authority_authority_id = Column(BigInteger, comment="角色ID")
