import sqlite3
import os

BasePath = 'college.db'

class DatabaseManager:
    def __init__(self, base_path: str):
        self.base_path = base_path

    def checkDatabase(self, sql_file: str) -> None:
        if not os.path.exists(self.base_path):
            print("INFO: Creating DB")

            connection = sqlite3.connect(self.base_path)
            connection.close()

            self._executeSQL(sql_file)

           # self._executeSQL('src/database/fill.sql')

    def _executeSQL(self, sql_file: str):
        connection = sqlite3.connect(self.base_path)
        cur = connection.cursor()

        with open(sql_file, 'r') as file:
            scripts = file.read()
            try:
                cur.executescript(scripts)
                connection.commit()
            except sqlite3.Error as error:
                print(error)
            finally:
                connection.close()

    def execute(self, query: str, args: tuple[str] = None, many: bool = False):
        connection = sqlite3.connect(self.base_path, isolation_level=None)
        cur = connection.cursor()

        try:
            if not many:
                res = cur.execute(query, args).fetchone()
            else:
                res = cur.execute(query).fetchall()
        except sqlite3.IntegrityError:
            connection.close()
            return {'error': 'request contains unique error'}

        connection.commit()
        connection.close()
        return res


db = DatabaseManager(BasePath)
