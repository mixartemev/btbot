from sqlalchemy import func
from models import *


class History(Base):
    __tablename__ = 'history'

    stamp = Column(DateTime, primary_key=True, default=func.now())
    rate = Column(DECIMAL(5, 2))

    def __init__(self, stamp, rate):
        self.stamp = stamp
        self.rate = rate
