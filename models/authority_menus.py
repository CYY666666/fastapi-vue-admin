
from models.base import Base
from sqlalchemy import Column, BigInteger, String, DateTime, Boolean
from datetime import datetime
from utils.snow_flake import generate_id


class Menus(Base):
    __tablename__ = "sys_authority_menus"
    __table_args__ = ({"comment": "权限菜单"})
    id = Column(BigInteger, primary_key=True, index=True)
    sys_base_menu_id = Column(BigInteger, comment="菜单ID")
    sys_authority_authority_id = Column(BigInteger, comment="角色ID")
