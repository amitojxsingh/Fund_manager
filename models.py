import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    total_pool_amount = Column(Float, default=400_000)
    loss = Column(Float, default=0)
    profit = Column(Float, default=0)
    effective_contribution = Column(Float, default=20_000)
    committee_value = Column(Float, default=400_000)

class MonthlyAllocation(Base):
    __tablename__ = 'monthly_allocations'
    id = Column(Integer, primary_key=True)
    month = Column(Integer, nullable=False)
    winning_member_id = Column(Integer, ForeignKey('members.id'))
    bid_loss = Column(Float, default=0)
    total_pool_amount = Column(Float, default=400_000)

    winning_member = relationship("Member", back_populates="allocations")

Member.allocations = relationship("MonthlyAllocation", order_by=MonthlyAllocation.id, back_populates="winning_member")

# Database setup
engine = create_engine('sqlite:///committee_fund.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
