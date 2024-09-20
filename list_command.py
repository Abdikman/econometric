from statistics import mean


def list_mean_update(list_for_mean: list):
    """Возвращает среденее значение"""
    return mean(list_for_mean)

def create_list_xy(list_x: list, list_y: list):
    """Создаёт и возвращает список y*x"""
    list_xy = []
    for i in range(len(list_x)):
        list_xy.append(list_x[i]*list_y[i])

    return list_xy

def create_list_square(list_values: list):
    """Создаёт и возвращает список значений в степени"""
    list_values_square = []
    for i in list_values:
        list_values_square.append(i**2)

    return list_values_square


