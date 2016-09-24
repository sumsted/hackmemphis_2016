from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, Text, Boolean

from db_setup import DbSetup

db_setup = DbSetup()
Base = db_setup.base


def to_list_of_dicts(lm):
    return [to_dict(m) for m in lm]


def to_dict(m):
    return {c.name: make_serializable(getattr(m, c.name)) for c in m.__table__.columns}


def make_serializable(v):
    if isinstance(v, datetime):
        return v.strftime("%m-%d-%Y %H:%M:%S")
    else:
        return v


class Authorizations(Base):
    __tablename__ = 'authorizations'
    authorization_id = Column(Integer(), primary_key=True)
    access_token = Column(Text())
    scope = Column(Text())
    team_name = Column(Text())
    team_id = Column(Text(), index=True)
    user_id = Column(Text())
    ok = Column(Boolean())
    created = Column(DateTime(), default=datetime.now, index=True)
    user_name = Column(Text())

    def __init__(self,access_token=None, scope=None, team_name=None, team_id=None, user_id=None, ok=None, user_name=None):
        self.access_token = access_token
        self.scope = scope
        self.team_name = team_name
        self.team_id = team_id
        self.user_id = user_id
        self.ok = ok
        self.user_name = user_name


class Debug(Base):
    __tablename__ = 'debug'
    debug_id = Column(Integer(), primary_key=True)
    step = Column(Text(), index=True)
    value = Column(Text())
    created = Column(DateTime(), default=datetime.now, index=True)

    def __init__(self, step=None, value=None):
        self.step = step
        self.value = value
