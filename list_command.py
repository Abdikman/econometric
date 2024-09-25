from statistics import mean
from math import sqrt


def create_list_mean(y: list, x: list):
    """Возвращает среденее значение"""
    list_mean = [mean(y), mean(x)]
    return list_mean

def create_list_sum(y: list, x: list):
    """Возвращает среденее значение"""
    list_sum = [sum(y), sum(x)]
    return list_sum

def create_list_xy(list_x: list, list_y: list, list_mean: list, list_sum: list):
    """Создаёт и возвращает список y*x"""
    list_xy = []
    for i in range(len(list_x)):
        list_xy.append(list_x[i]*list_y[i])

    list_mean.append(mean(list_xy))
    list_sum.append(sum(list_xy))
    return list_xy

def create_list_square(list_values: list, list_mean: list, list_sum: list):
    """Создаёт и возвращает список значений в степени"""
    list_values_square = []
    for i in list_values:
        list_values_square.append(i**2)

    list_mean.append(mean(list_values_square))
    list_sum.append(sum(list_values_square))
    return list_values_square

def create_regress_coeff(self):
    """Вычисляет переменную b"""
    b = self.list_mean[2] - self.list_mean[0] * self.list_mean[1]
    c = self.list_mean[3] - self.list_mean[1]**2

    return b/c

def create_konst(self):
    """Вычисляет переменную a"""
    a = self.list_mean[0] - self.b * self.list_mean[1]

    return abs(a)

def create_Yx(self, list_mean: list, list_sum: list):
    """Вычисляет переменную list_Yx"""
    list_Yx = []
    for i in self.list_x:
        list_Yx.append(self.a + self.b * i)

    list_mean.append(mean(list_Yx))
    list_sum.append(sum(list_Yx))
    return list_Yx

def create_list_y_Yx_square(self, list_mean: list, list_sum: list):
    """(y-Yx) в куадрат"""
    list_y_Yx_square = []

    for i in range(len(self.list_y)):
        list_y_Yx_square.append((self.list_y[i] - self.list_Yx[i])**2)

    list_mean.append(mean(list_y_Yx_square))
    list_sum.append(sum(list_y_Yx_square))
    return list_y_Yx_square



