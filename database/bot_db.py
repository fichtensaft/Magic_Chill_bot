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

    def insert_user_id(self, user_id):
        user_id_req = """INSERT INTO events(user_id) VALUES (?)"""
        self.execute(user_id_req, (user_id, ))

        event_id = self.get_event_id()
        return event_id

    def insert_date(self, cur_date, event_id):
        date_req = """INSERT INTO events(date_column) VALUES (?) WHERE event_id = ?"""
        self.execute(date_req, (cur_date, event_id))

    # Testing site
    def check_numbers(self, user_id):
        sql_check_req = """SELECT number_column FROM events WHERE user_id = (?)"""
        self.execute(sql_check_req, (user_id, ))
        result = self.cur.fetchone()

        return result[0]

    def insert_number(self, user_id):
        if self.check_numbers(user_id):
            sql_get_num_req = """SELECT number_column FROM events WHERE user_id = (?) ORDER BY number_column DESC"""
            self.execute(sql_get_num_req, (user_id, ))
            last_num = self.cur.fetchone()
            print(last_num)

            sql_ins_num_req = """INSERT INTO events(number_column) VALUES (?)"""
            self.execute(sql_ins_num_req, (last_num+1, ))

        else:
            self.execute("""INSERT INTO events(number_column) VALUES (1)""")

    def get_event_id(self):
        self.execute("""SELECT event_id FROM events ORDER BY event_id DESC LIMIT 1""")
        event_id = self.cur.fetchone()
        print("Event id:", event_id[0])

        return event_id[0]
