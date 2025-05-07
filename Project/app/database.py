from sqlmodel import SQLModel, create_engine

#! SQLite file name
sqlite_file_name = "database.db"
DATABASE_URL = f"sqlite:///{sqlite_file_name}"


#! Create engine
engine = create_engine(DATABASE_URL, echo=True)


#! Initialize DB
def create_db_and_table():
    SQLModel.metadata.create_all(engine)
