
class FileReader:

    def __init__(self, name):
        self.name = name

    def read(self):
        file_name = self.name
        try:
            with open(file_name, 'r') as f:
                string = f.read()
        except IOError as err:
            return ''
        else:
            return string


reader = FileReader(input('Please enter a file name: '))
print(reader.read())
for i in reader.read():
    print(i)