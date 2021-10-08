from models.base import Base
from sqlalchemy import Column, BigInteger, String, DateTime, Boolean
from datetime import datetime
from utils.snow_flake import generate_id


class Menus(Base):
    __tablename__ = "sys_base_menus"
    __table_args__ = ({"comment": "菜单"})
    id = Column(BigInteger, primary_key=True, index=True)
    menu_level = Column(BigInteger, index=True)
    parent_id = Column(BigInteger, nullable=False, default=0, comment="父菜单ID")
    path = Column(String(191), nullable=False, comment="路由path")
    name = Column(String(191), nullable=False, comment="路由name")
    hidden = Column(Boolean, nullable=False, comment="是否在列表隐藏")
    component = Column(String(191), nullable=False, comment="对应前端文件路径")
    sort = Column(BigInteger, nullable=False, index=True, comment="排序标记")
    keep_alive = Column(Boolean, nullable=False, index=True, comment="附加属性")
    default_menu = Column(Boolean, nullable=False, index=True, comment="附加属性")
    title = Column(String(191), nullable=False, comment="名称")
    icon= Column(String(191), nullable=False, comment="图标")
    close_tab = Column(Boolean, nullable=False, comment="附加属性")
