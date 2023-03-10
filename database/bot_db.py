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

    def insert_memo_values(self, *args: str):
        """

        :param args:
        :return:
        """
        sql_req = """INSERT INTO events(user_id, number, date, places, people, state, memes) 
        VALUES (?, ?, ?, ?, ?, ?, ?)"""
        self.execute(sql_req, args)

    # Testing site
    def get_new_event_number(self, user_id):
        sql_req = """SELECT number FROM events WHERE user_id =(?) ORDER BY number DESC"""
        self.execute(sql_req, (user_id, ))
        result = self.cur.fetchone()
        event_num = result[0]

        if event_num:
            return event_num+1
        else:
            return 0

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
