import sqlite3 as sq


class BotDB:
    __DB_NAME = r"C:\Me\Coding_Python\Projects\Magic_Chill\database\chill_base.db"

    def __init__(self):
        self.conn = sq.connect(self.__DB_NAME)
        self.cur = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        if isinstance(exc_val, Exception):
            self.conn.rollback()
        else:
            self.conn.commit()

        self.conn.close()

    def execute(self, sql_req, params=None):
        self.cur.execute(sql_req, params or ())

    def create_events_table(self):
        self.execute("""CREATE TABLE IF NOT EXISTS events(
                event_id INTEGER PRIMARY KEY,
                user_id INT,
                number INT,
                date DATE,
                places TEXT,
                people TEXT,
                state TEXT,
                memes TEXT
            )"""
                     )

    def drop_table_events(self):
        drop_req = """DROP TABLE events"""
        self.execute(drop_req)

    def insert_memo_values(self, *args: str) -> None:
        sql_req = """INSERT INTO events(user_id, number, date, places, people, state, memes) 
        VALUES (?, ?, ?, ?, ?, ?, ?)"""
        self.execute(sql_req, args)

    def get_new_event_number(self, user_id):
        sql_req = """SELECT number FROM events WHERE user_id =(?) ORDER BY number DESC LIMIT 1"""
        self.execute(sql_req, (user_id, ))
        result = self.cur.fetchone()
        if result:
            return result[0] + 1
        else:
            return 1

    # test_zone
    def fetch_dates(self, user_id):
        sql_req = """SELECT date FROM events WHERE user_id"""