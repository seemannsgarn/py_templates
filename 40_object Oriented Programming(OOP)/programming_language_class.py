class Programming_language:

    def __init__(self,name,ide):
        self.name = name
        self.ide = ide

    def writting(self):
        print(f'This code on {self.name} is writting. That be good!')

    def crashes(self):
        print(f'This code on {self.name} is crashes, please fix it!')