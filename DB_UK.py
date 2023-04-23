import sqlite3


class Db:

    def __init__(self):
        self.conn = sqlite3.connect('uk_inftactructure.db')
        self.cur = self.conn.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS vmb(
                            id INTEGER PRIMARY KEY,
                            NAME CHAR(50),
                            lat REAL,
                            lon REAL,
                            IMPORTANCE CHAR(100),
                            SHORT_INFO TEXT,
                            FULL_INFO TEXT
                            );
                        """)
        self.conn.commit()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS avb(
                            id INTEGER PRIMARY KEY,
                            NAME CHAR(50),
                            lat REAL,
                            lon REAL,
                            IMPORTANCE CHAR(100),
                            SHORT_INFO TEXT,
                            FULL_INFO TEXT
                            );
                        """)
        self.conn.commit()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS vg(
                            id INTEGER PRIMARY KEY,
                            NAME CHAR(50),
                            lat REAL,
                            lon REAL,
                            IMPORTANCE CHAR(100),
                            SHORT_INFO TEXT,
                            FULL_INFO TEXT
                            );
                        """)
        self.conn.commit()

    def db_cleaning(self):
        self.cur.execute("""DELETE FROM vmb;""")
        self.conn.commit()
        print('Ok')

    def insert_into_db(self, new_line):
        self.cur.execute("INSERT INTO vmb VALUES(NULL, ?, ?, ?, ?);", new_line)
        self.conn.commit()
        print('Ok')

    def read_db_vmb(self):
        self.cur.execute("""SELECT * FROM vmb;""")
        records_vmb = self.cur.fetchall()
        return records_vmb
    
    def read_db_avb(self):
        self.cur.execute("""SELECT * FROM avb;""")
        records_avb = self.cur.fetchall()
        return records_avb
    
    def read_db_vg(self):
        self.cur.execute("""SELECT * FROM vg;""")
        records_vg = self.cur.fetchall()
        return records_vg
    
    def read_one_note(self, obj_type, name):

        if obj_type == 'Военно-морская база':
            self.cur.execute("""SELECT * FROM vmb WHERE NAME = ?;""", (name, ))
            record = self.cur.fetchone()

        if obj_type == 'Авиационная база':
            self.cur.execute("""SELECT * FROM avb WHERE NAME = ?;""", (name, ))
            record = self.cur.fetchone()

        if obj_type == 'Военный городок':
            self.cur.execute("""SELECT * FROM vg WHERE NAME = ?;""", (name, ))
            record = self.cur.fetchone()

        if record:
            return record


# db = Db()
# db.db_cleaning()
# db.insert_into_db(['ВМБ Клайд', 56.067822, -4.817431, 'Some info'])
# db.read_db()
# db.read_one_note('ВМБ Клайд')

