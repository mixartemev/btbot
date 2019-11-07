from sqlalchemy import func
from models import *


class History(Base):
    __tablename__ = 'history'

    stamp = Column(DateTime, primary_key=True, default=func.now())
    rate = Column(DECIMAL(5, 2))

    def __init__(self, rate):
        self.rate = rate
