import sqlite3, datetime
from task import Task

class Database():
    def __init__(self):
        self.connection = self.__init_db()
        self.__init_tables()
        self.connection.commit()
    
    def __init_db(self):
        return sqlite3.connect('task.db', check_same_thread=False)

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
    
    def delete_task(self, uuid):
        insert_query = "DELETE FROM WHERE uuid = :uuid"
        self.connection.execute(insert_query, {"uuid": uuid})
        self.connection.commit()

    def get_task(self, uuid):
        get_one_query = "SELECT * FROM tasks WHERE uuid=:uuid LIMIT 1"
        result = self.connection.execute(get_one_query, {"uuid": uuid})
        return self.__createTask(result.fetchone())

    def get_all_tasks(self):
        get_all_query = "SELECT * FROM tasks"
        result = self.connection.execute(get_all_query)
        return self.__createTasks(result.fetchall())

    def get_all_tasks_left(self):
        get_all_left_query = "SELECT * FROM tasks WHERE done = 0"
        result = self.connection.execute(get_all_left_query)
        return self.__createTasks(result.fetchall())

    def __createTask(self, db_output):
        if len(db_output) != 6:
            return Task()
        else:
            return Task(uuid=db_output[0], title=db_output[1],comment=db_output[2],created_at=datetime.datetime.fromisoformat(db_output[3]),last_updated=datetime.datetime.fromisoformat(db_output[4]),done=db_output[5])

    def __createTasks(self, db_output):
        task_list = []
        for item in db_output:
            task_list.append(self.__createTask(item))
        return task_list
