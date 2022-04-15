from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from task import Task
from database import Database
import uuid, datetime

app = Flask(__name__)
api = Api(app)

db = Database()

def abort_if_todo_doesnt_exist(task, uuid):
    if task == None:
        abort(404, error="Task {} doesn't exist".format(uuid))

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('comment')
parser.add_argument('done')


# Task
# shows a single task item and lets you delete a todo item
class Tasks(Resource):
    def get(self, task_id):
        task = db.get_task(task_id)
        abort_if_todo_doesnt_exist(task, task_id)
        return task.get_output_dict()

    def delete(self, task_id):
        task = db.get_task(task_id)
        abort_if_todo_doesnt_exist(task, task_id)
        db.delete_task(task_id)
        return '', 204

    def put(self, task_id):
        task = db.get_task(task_id)
        abort_if_todo_doesnt_exist(task, task_id)
        args = parser.parse_args()
        task = self.__update_task(args, task)
        db.update_task(task)
        return task.get_output_dict(), 201
    
    def __update_task(self, args, task):
        changed = False
        if len(args['title']) != 0:
            task.title = args['title']
            changed = True
        if len(args['comment']) != 0:
            task.comment = args['comment']
            changed = True
        if len(args['done']) != 0:
            task.done = bool(args['done'])
            changed = True
        if changed:
            updated = datetime.datetime.now()
            task.last_updated = updated
        return task

# TodoList
# shows a list of all remaining todos
class TodoList(Resource):
    def get(self):
        todo_list = db.get_all_tasks_left()
        output = {'tasks': get_dict_list(todo_list)}
        return output

# TaskList
# shows a list of all tasks, and lets you POST to add new tasks
class TasksList(Resource):
    def get(self):
        task_list = db.get_all_tasks()
        output = {'tasks': get_dict_list(task_list)}
        return output

    def post(self):
        args = parser.parse_args()
        new_id = str(uuid.uuid4())
        creation = datetime.datetime.now()
        task = Task(uuid=new_id, title=args['title'], comment=args['comment'], created_at=creation, last_updated=creation, done=False)
        db.add_task(task)
        return task.get_output_dict(), 201

def get_dict_list(task_list):
    output_list = []
    for task in task_list:
        output_list.append(task.get_output_dict())
    return output_list

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todo')
api.add_resource(TasksList, '/tasks')
api.add_resource(Tasks,     '/tasks/<task_id>')


if __name__ == '__main__':
    app.run(debug=True)