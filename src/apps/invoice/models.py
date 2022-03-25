from libs.database import Base
from sqlalchemy import (
    Column,
    Numeric,
    ForeignKey,
    Integer,
    String,
    DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, server_default=func.now())

    items = relationship("InvoiceItem", back_populates="invoice", cascade='all, delete, delete-orphan')


    def as_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'items': self.items
        }


class InvoiceItem(Base):
    __tablename__ = 'invoice_items'

    id = Column(Integer, primary_key=True)
    invoice = Column(Integer, ForeignKey('invoices.id'), nullable=False)
    units = Column(Integer, nullable=False)
    amount = Column(Numeric, nullable=False)
    description = Column(String, default='')


    def as_dict(self):
        return {
            'id': self.id,
            'units': self.units,
            'amount': self.amount,
            'description': self.description,
            'invoice': self.invoice
        }
