import json

class Task():
    def __init__(self, uuid, title, comment, created_at, last_updated, done):
        self.uuid = uuid
        self.title = title
        self.comment = comment
        self.created_at = created_at
        self.last_updated = last_updated
        self.done = done
    
    def get_dict(self):
        return {'uuid': self.uuid, 'title': self.title,'comment': self.comment,'created_at': self.created_at,'last_updated': self.last_updated,'done': self.done}

    def serialize(self)
        return json.dumps(self.get_dict())
