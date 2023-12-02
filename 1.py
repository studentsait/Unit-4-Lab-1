class Student:
    def __init__(self, name, id, address):
        self.name = name
        self.id = id
        self.address = address

    def display_information(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("Address:", self.address)

student1 = Student("kartikey", 38746, "34 9th avenue")
student1.display_information()