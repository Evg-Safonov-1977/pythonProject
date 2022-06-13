class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
petr = User('Petr Petrov', 'petr@mail.ru')
ivan = User('Ivan Ivanov', 'ivan@mail.ru')

print(petr.name)
print(petr.email)

print(ivan.name)
print(ivan.email)


class Event:
    def __init__(self, timestamp, event_type, session_id):
        self.timestamp = timestamp
        self.event_type = event_type
        self.session_id = session_id
events = [
    {
     "timestamp": 111,
     "type": "itemViewEvent",
     "session_id": "0:N1"
    },
    {
     "timestamp": 222,
     "type": "itemViewEvent",
     "session_id": "0:N2"
    },
    {
     "timestamp": 333,
     "type": "itemViewEvent",
     "session_id": "0:N3"
    },
]

for event in events:
    event_obj = Event(timestamp=event.get("timestamp"),
                      event_type=event.get("type"),
                      session_id=event.get("session_id"))
    print(event_obj.timestamp)