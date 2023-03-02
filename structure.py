import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import declarative_base


engine = create_engine('sqlite:///compensation.db')
Base = declarative_base()


class Info(Base):
    __tablename__ = 'Compensation data'
    id = Column(Integer, primary_key=True)
    plot_id = Column('Plot_id', String)
    sum_vol = Column('Commercial volume', Float)
    annual = Column('Annual compensation', Float)
    single = Column('Single compensation', Float)
    create_date = Column('Created_date', DateTime, default=datetime.datetime.utcnow)

    def __init__(self, plot_id, sum_vol, annual, single):
        self.plot_id = plot_id
        self.sum_vol = sum_vol
        self.annual = annual
        self.single = single

    def __repr__(self):
        return (
            f'No.: {self.id}| Plot_id: {self.plot_id}| Commercial volume: {self.sum_vol}| '
            f'Annual compensation: {self.annual}| Single compensation: {self.single}|'
            f'Created date: {self.create_date}'
        )


Base.metadata.create_all(engine)
