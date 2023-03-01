import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import declarative_base
import methods

engine = create_engine('sqlite:///compensation.db')
Base = declarative_base()


class Info(Base):
    __tablename__ = 'Compensation data'
    id = Column(Integer, primary_key=True)
    plot_id = Column('Plot_id', String)
    sum_lvol_total = Column('Commercial volume', Float)
    annual_comp = Column('Annual compensation', Float)
    single_comp = Column('Single compensation', Float)
    create_date = Column('Created_date', DateTime, default=datetime.datetime.utcnow)

    # def __init__(self, plot_id, sum_lvol_total, annual_comp, single_comp):
    #     self.plot_id = plot_id
    #     self.sum_lvol_total = sum_lvol_total
    #     self.annual_comp = annual_comp
    #     self.single_comp = single_comp
    #
    # def __repr__(self):
    #     return (
    #         f'No.: {self.id}| Plot_id: {self.plot_id}| Commercial volume: {self.sum_lvol_total}| '
    #         f'Annual compensation: {self.annual_comp}| Single compensation: {self.single_comp}|'
    #         f'Created date: {self.create_date}'
        )


Base.metadata.create_all(engine)
