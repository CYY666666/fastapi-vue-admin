from models.base import Base
from sqlalchemy import Column, BigInteger, String, DateTime
from utils.snow_flake import generate_id
from datetime import datetime


class Permission(Base):
    __tablename__ = "permission"
    __table_args__ = ({"comment": "权限表"})
    perm_id = Column(BigInteger, default=generate_id, index=True, primary_key=True, unique=True)
    perm_name = Column(String(50), nullable=False, unique=True, comment="权限名称")
    perm_interface = Column(String(100), nullable=False, unique=True, comment="权限对应的接口")
    created_at = Column(DateTime(), default=datetime.now, comment="创建时间")
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now, comment="最后一次更新时间")

    def __repr__(self):
        return f"Permission:{self.perm_name}"
