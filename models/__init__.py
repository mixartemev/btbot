from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DECIMAL, DateTime

__version__ = '1.0'
__all__ = ["Base", "Column", "DECIMAL", "DateTime"]

# Load Base class for declarative way tables operating
Base = declarative_base()
