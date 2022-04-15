import json, datetime

class Task():
    def __init__(self, uuid, title, comment, created_at, last_updated, done):
        self.uuid = uuid
        self.title = title
        self.comment = comment
        self.created_at = datetime.datetime.fromisoformat(created_at)
        self.last_updated = datetime.datetime.fromisoformat(last_updated)
        self.done = bool(done)
    
    def get_db_dict(self):
        return {'uuid': self.uuid, 'title': self.title,'comment': self.comment,'created_at': self.created_at.isoformat(),'last_updated': self.last_updated.isoformat(),'done': int(self.done)}
    
    def get_dict(self):
        return {'uuid': self.uuid, 'title': self.title,'comment': self.comment,'created_at': self.created_at,'last_updated': self.last_updated,'done': self.done}

    def serialize(self):
        return json.dumps(self.get_dict())
