import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import declarative_base


engine = create_engine('sqlite:///compensation.db')
Base = declarative_base()


class Info(Base):
    __tablename__ = 'Compensation data'
    id = Column(Integer, primary_key=True)
    tree_volume = Column('2', String)
    t_price = Column('7', Float)
    single = Column('8', Float)
    annual = Column('9', Float)
    create_date = Column('Created_date', DateTime, default=datetime.datetime.utcnow)

    # TODO FIX
    def __init__(self, tree_volume, t_price, single_compensation, annual_compensation):
        self.tree_volume_list = tree_volume
        self.t_price = t_price
        self.single_compensation = single_compensation
        self.annual_compensation = annual_compensation

    # def __repr__(self):
    #     return (
    #         f'No.: {self.id}| Plot_id: {self.plot_id}| Commercial volume: {self.sum_vol}| '
    #         f'Annual compensation: {self.annual}| Single compensation: {self.single}|'
    #         f'Created date: {self.create_date}'
    #     )


Base.metadata.create_all(engine)
