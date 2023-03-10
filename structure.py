import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///compensation.db', echo=True)
Base = declarative_base()


class Info(Base):
    __tablename__ = 'Compensation data'
    id = Column(Integer, primary_key=True)
    tree_volume = Column('2', String)
    t_price = Column('7', Float)
    single_compensation = Column('8', Float)
    annual_compensation = Column('9', Float)
    create_date = Column('Created_date', DateTime, default=datetime.datetime.utcnow)

    # TODO FIX
    def __init__(self, tree_volume, t_price, single_compensation, annual_compensation):
        self.tree_volume = tree_volume
        self.t_price = t_price
        self.single_compensation = single_compensation
        self.annual_compensation = annual_compensation

    def __repr__(self):
        return (
            f'No.: {self.id}| 2: {self.tree_volume}| 7: {self.t_price}| '
            f'8: {self.single_compensation}| 9: {self.annual_compensation}|'
            f'Created date: {self.create_date}'
        )


Base.metadata.create_all(bind=engine)
