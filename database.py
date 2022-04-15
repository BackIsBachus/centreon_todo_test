import sqlite3

class Database():
    def __init__(self):
        self.connection = self.__init_db()
        self.__init_tables()
        self.connection.commit()
    
    def __init_db(self):
        return sqlite3.connect('task.db')

    def __init_tables(self):
        self.connection.execute('''CREATE TABLE IF NOT EXISTS tasks (uuid text, title text, comment text, created_at text, last_updated text, done integer)''')

    def add_task(self, task):
        insert_query = "INSERT INTO tasks VALUES (:uuid, :title, :comment, :created_at, :last_updated, :done)"
        values = task.get_db_dict()
        self.connection.execute(insert_query, values)
        self.connection.commit()

    def update_task(self, task):
        insert_query = "UPDATE tasks SET title = :title, comment = :comment, created_at = :created_at, last_updated = :last_updated, done = :done WHERE uuid = :uuid"
        values = task.get_db_dict()
        self.connection.execute(insert_query, values)
        self.connection.commit()
        
    def get_task(self, uuid):
        get_one_query = "SELECT * FROM tasks WHERE uuid=:uuid LIMIT 1"
        result = self.connection.execute(get_one_query, {"uuid: uuid"})
        return result.fetchone()

    def get_all_tasks(self):
        get_all_query = "SELECT * FROM tasks"
        result = self.connection.execute(get_all_query)
        return result.fetchall()

    def get_all_tasks_left(self):
        get_all_left_query = "SELECT * FROM tasks WHERE done = 0"
        result = self.connection.execute(get_all_left_query)
        return result.fetchall()