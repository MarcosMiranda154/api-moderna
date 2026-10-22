from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

SQLiteBase = declarative_base()

class SQLiteClient:
    database_path = "sqlite:///db/database.db"
    
    def __init__(self):
        self._engine = create_engine(self.database_path, echo=True)
        self._session = sessionmaker(bind=self._engine, autocommit=False, autoflush=False)
    
    def __call__(self):
        session_local = self._session()
        try:
            yield session_local
        finally:
            yield session_local.close()
    
    def _get_engine(self) -> Session:
        return next(self.__call__())    