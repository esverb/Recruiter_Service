from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime

from sqlalchemy.sql.sqltypes import Date


class JobBase(BaseModel):
    title: Optional[str] = None
    contact: Optional[str] = None
    department: Optional[str] = None
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()

class JobCreate(JobBase):
    title: str
    contact: str
    department: str
    description: str


class ShowJob(JobBase):
    title: str
    contact: Optional[str]
    department: str
    description: str
    date_posted: Optional[date]
    class Config():
        orm_mode = True