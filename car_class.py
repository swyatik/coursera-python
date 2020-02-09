import os
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_file_photo_ext(self):
        # розбиваємо назву файла на назву і розширення, і беремо тільки розширення
        # os.path.splitext() - повертає tuple з двох елементів (назва і розширення)
        return os.path.splitext(self.photo_file_name)[1]

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl

    def get_body_volume(self):
        # повертаємо об'єм кузова Truck
        return self.body_whl[0]*self.body_whl[1]*self.body_whl[2]


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    try:
        with open(csv_filename) as f: # відкриваємо файл
            reader = csv.reader(f, delimiter=';') # читаємо файл
            next(reader) # пропускаємо рядок заголовок
            for row in reader: # перебираємо наступні рядки в циклі
                if len(row) == 7:
                    car_list.append(row)
    except FileNotFoundError:
        print("No such file or directory: {}".format(csv_filename))

    # перетворюємо 2колонку в int, 4 в список i float, 5 в float
    for i in range(len(car_list)):
        for j in range(len(car_list[i])):
            try:
                if j == 2 and car_list[i][2] != '':
                    car_list[i][2] = int(car_list[i][2])
            except ValueError:
                print("Date error: file - {0}, row - {1}: кількість пасажирів має бути число!".format(csv_filename, i))
            try:
                if j == 4:
                    if car_list[i][4] != '':
                        l_4 = car_list[i][4].split('x')
                        car_list[i][4] = [float(l_4[0]), float(l_4[1]), float(l_4[2])]
                    else:
                        car_list[i][4] = [0.0, 0.0, 0.0]
            except ValueError:
                print("Date error: file - {0}, row - {1}: параметри кузова мають бути число!".format(csv_filename, i))
            try:
                if j == 5 and car_list[i][5] != '':
                    car_list[i][5] = float(car_list[i][5])
            except ValueError:
                print("Date error: file - {0}, row - {1}: вантажопідйомність має бути число!".format(csv_filename, i))

    return car_list



#print(get_car_list('coursera_week3_cars.csv'))
#print(get_car_list('c1.csv'))
#print(get_car_list('c2.csv'))
#print(get_car_list('c3.csv'))
print(get_car_list('c4.csv'))