class BaseEntity:
    def __init__(self):
        pass

class Hostel(BaseEntity):
    id_counter = 1
    def __init__(self, name, cordinates):
        super().__init__()
        self.name = name
        self.location_cordinates = cordinates
        self.id = Hostel.id_counter
        Hostel.id_counter += 1

class User(BaseEntity):
    id_counter = 1
    def __init__(self, name, email, room, hostel_id,role):
        self.name = name
        self.email = email
        self.role = role
        self.room = room
        self.hostel_id = hostel_id
        self.id = User.id_counter
        User.id_counter += 1