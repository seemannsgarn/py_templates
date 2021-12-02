class Programming_language:

    usage = 'Web'

    def __init__(self,name,ide):
        self.name = name    # instance variable
        self.ide = ide      # instance variable

    def writting(self):
        print(f'This code on {self.name} is writting. That be good!')

    def crashes(self):
        print(f'This code on {self.name} is crashes, please fix it!')