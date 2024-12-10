from enum import Enum
from datetime import date

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase): pass


class PartnerType(Enum):
    ZAO = "ЗАО"
    OOO = "ООО"
    OAO = "ОАО"
    PAO = "ПАО"


class Partner(Base):
    __tablename__ = "partners"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped["PartnerType"]
    name: Mapped[str]
    director: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str] = mapped_column(String(13))
    address: Mapped[str]
    inn: Mapped[str] = mapped_column(String(10))
    rate: Mapped[int]


class ProductType(Base):
    __tablename__ = "product_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    ratio: Mapped[float]


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    type_id: Mapped[int] = mapped_column(ForeignKey("product_types.id", ondelete="CASCADE"))
    type: Mapped["ProductType"] = relationship()
    name: Mapped[str]
    article: Mapped[int] = mapped_column(unique=True)
    min_cost: Mapped[float]


class Sale(Base):
    __tablename__ = "sales"

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"), primary_key=True)
    product: Mapped["Product"] = relationship()
    partner_id: Mapped[int] = mapped_column(ForeignKey("partners.id", ondelete="CASCADE"), primary_key=True)
    partner: Mapped["Partner"] = relationship()
    count: Mapped[int]
    sale_date: Mapped[date]


class MaterialType(Base):
    __tablename__ = "material_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    defective_percentage: Mapped[float]
