import tempfile

class File:
    def __init__(self, file_path):
        self.file_path = file_path # шлях до файлу
        self.result_line = None # string рядок, що повертається при ітерації
        self.size = None # кількість байт у файлі
        self.size_read_line = 0 # кількість прочитаних байт
        with open(self.file_path, 'r') as f: # перевіряємо чи файл порожній
            if f.read() == '':
                self.size = 0
            else:
                f.seek(0, 2) #курсор в кінець файлу
                self.size = f.tell() # рахує кількість байт у файлі

    def __str__(self):
        return self.file_path # повертає шлях до файлу при виклику: print

    def __iter__(self):
        return self

    def __next__(self): # переоприділяємо ітератор
        if self.size_read_line == self.size or self.size_read_line > self.size:
            raise StopIteration
        else:
            with open(self.file_path) as f:
                f.seek(self.size_read_line) # курсор в кінець прочитаних байтів
                self.result_line = f.readline() # читаємо рядок
                self.size_read_line = f.tell() # рахуємо кількість прочитаних байтів
        return self.result_line # повертаємо рядок

    def __add__(self, obj):
        name_1 = self.file_path.split('/')[-1:] # виділяємо назву файлу з шляху до нього
        name_2 = obj.file_path.split('/')[-1:]
        name_new = ('.').join(name_1[0].split('.')[:-1]) + '_' + name_2[0] # створюємо нове ім'я файлу
        file_path_new = '/'.join(tempfile.gettempdir().split('\\')) + '/' + name_new # шлях до нового файлу
        # записуємо почергово дані з 1 та 2 файлів до нового
        with open(file_path_new, 'w') as f:
            f.write((open(self.file_path, 'r')).read())
        with open(file_path_new, 'a') as f:
            if self.size != 0:
                f.write('\n')
            f.write((open(obj.file_path, 'r')).read())
        # створюємо новий об'єкт ш повертаємо його з метода
        new_obj = File(file_path_new)
        return new_obj

    def write(self, text): # дозапис даних у файл
        if self.size == 0:
            with open(self.file_path, 'w') as f:
                f.write(text)
                self.size = f.tell()
        else:
            with open(self.file_path, 'a') as f:
                f.write('\n' + text)
                self.size = f.tell()
        return True

file1 = File('/ROBOTA/DEVELOP/Coursera_ubuntu/cours/aca.txt')
file2 = File('/ROBOTA/DEVELOP/Coursera_ubuntu/cours/large.txt')
file3 = File('/ROBOTA/DEVELOP/Coursera_ubuntu/cours/test3.txt')
file4 = File('/ROBOTA/DEVELOP/Coursera_ubuntu/cours/test2.txt')

print(file4)
file_new = file4 + file1
print(file4.size)
print(file4.file_path)

"""
a = 0
for i in file_new:
    a += 1
    print(a, '-', i, end='')

file_new.write('i make it !')
"""

