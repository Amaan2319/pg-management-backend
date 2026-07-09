import datetime


class BaseEntity:
    def __init__(self):
        pass

    def papaMethod(self):
        return "This is a method from the parent class"

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
    def getUserInfo(self):
        return f"User: {self.name}, Hostel: {self.hostel_id}, Room: {self.room}, Role: {self.role}"
    
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}', room='{self.room}', hostel_id={self.hostel_id}, role='{self.role}')"
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        self._email = value
    
    def __eq__(self,other):
        if not isinstance(other,User):
            return f"Cannot compare User with {type(other)}"
        return self.hostel_id == other.hostel_id and self.room == other.room

    def papaMethod(self):
        print(super().papaMethod())
        return f"And this is a method from the child class"

amaan = User("Amaan", "amaan@example.com", "Room 101", 1, "student")
abbas = User("Abbas", "abbas@example.com", "Room 102", 2, "student")

print(amaan.email)
print(amaan==abbas)
print(amaan.papaMethod())

