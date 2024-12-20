from datetime import date

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from database.database import SessionFactory


class Base(DeclarativeBase): pass


class Partner(Base):
    __tablename__ = "partners"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str]
    name: Mapped[str]
    director: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str] = mapped_column(String(13))
    address: Mapped[str]
    inn: Mapped[str] = mapped_column(String(10))
    rate: Mapped[int]

    @property
    def discount(self) -> int:
        sales_count = 0
        for product in self.sales:
            sales_count += product.count
        if 10000 < sales_count <= 50000:
            return 5
        elif 50000 < sales_count <= 300000:
            return 10
        elif 300000 < sales_count:
            return 15
        return 0

    @property
    def sales(self):
        with SessionFactory() as session:
            return session.query(Sale).filter(Sale.partner == self).all()

    def save(self):
        with SessionFactory() as session:
            session.add(self)
            session.commit()

    @staticmethod
    def get_all():
        with SessionFactory() as session:
            return session.query(Partner).all()


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

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"))
    product: Mapped["Product"] = relationship()
    partner_id: Mapped[int] = mapped_column(ForeignKey("partners.id", ondelete="CASCADE"))
    partner: Mapped["Partner"] = relationship()
    count: Mapped[int]
    sale_date: Mapped[date]


class MaterialType(Base):
    __tablename__ = "material_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    defective_percentage: Mapped[float]
