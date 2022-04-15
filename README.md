# Basic REST todo app coding test

Basic REST todo app coding test. Not made to but a complete product but only an initial step basic step. Made using Flask-RESTful.

To run locally, go in the folder after cloning and run
`pip install requirements.txt`
and then
`python api.py`

You can then, by default, hit the API on `localhost:5000`.

## API structure

### Task return object

```json
{
    "uuid": "e59e10d1-c988-4028-80d7-16cfe5436609",
    "title": "title",
    "comment": "comment",
    "created_at": "2022-04-15T19:57:22.163954",
    "last_updated": "2022-04-15T20:23:28.929640",
    "done": true
}
```


### /todo

GET - Returns the list of tasks that have not been done/finished.

### /tasks

GET - Returns the list of all tasks done or not.
POST - Create a new task to do with a title and comment
```json
{
    "title": "title",
    "comment": "comment"
}
```

### /tasks/<task_id>

GET - Returns the task matching the uuid provided
PUT - Updates the task matching the uuid provided (all fields are optional)
```json
{
    "title": "title",
    "comment": "comment",
    "done": true
}
```
DELETE - Deletes the task matching the uuid provided