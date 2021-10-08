from models.base import Base
from sqlalchemy import Column, BigInteger, String, DateTime, Boolean
from datetime import datetime
from utils.snow_flake import generate_id


class Menus(Base):
    __tablename__ = "sys_users"
    __table_args__ = ({"comment": "用户"})
    id = Column(BigInteger, primary_key=True, index=True)
    uuid = Column(String(191), nullable=False, comment="用户UUID")
    username = Column(String(191), nullable=False, comment="用户登录名")
    password = Column(String(191), nullable=False, comment="用户登录密码")
    nick_name = Column(String(191), nullable=False, comment="用户昵称")
    side_mode = Column(String(191), nullable=False, comment="用户侧边主题")
    header_img = Column(String(191), nullable=False, comment="用户头像")
    base_color = Column(String(191), nullable=False, comment="基础颜色")
    active_color = Column(String(191), nullable=False, comment="活跃颜色")
    authority_id = Column(BigInteger, nullable=False, comment="用户角色ID")
