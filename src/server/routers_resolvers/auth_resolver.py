from src.database.db_manager import db

def login(name: str, password: str):

    res = db.execute(
        query=f'select * from Users where login=(?) and password =(?)',
        args=(name, password)
    )
    return res
