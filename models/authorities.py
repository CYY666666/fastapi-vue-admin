from models.base import Base
from sqlalchemy import Column, BigInteger, String, DateTime, Text
from datetime import datetime
from utils.snow_flake import generate_id


class Authorities(Base):
    __tablename__ = "sys_authorities"
    __table_args__ = ({"comment": "角色"})
    id = Column(BigInteger, primary_key=True, index=True)
    authority_name = Column(String(191), nullable=False, index=True, comment="角色名")
    parent_id = Column(BigInteger, nullable=False, default=0, comment="父角色ID")
    default_router = Column(String(191), nullable=False, comment="默认菜单")
