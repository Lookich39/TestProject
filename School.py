class students():
    def __init__(self, surname, initials, num_group, progress):
        self.surname = surname
        self.initials = initials
        self.num_group = num_group
        self.progress = progress
    def show(self):
        print(self.surname)
        print(self.initials)
        print(self.num_group)
        print(self.progress)

ivan = students("ivanov", "I I", 15, [1, 2, 4, 5])
ivan.show()
