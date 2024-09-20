from statistics import mean


def create_list_mean(y: list, x: list):
    """Возвращает среденее значение"""
    list_mean = [mean(y), mean(x)]
    return list_mean

def create_list_xy(list_x: list, list_y: list, list_mean: list):
    """Создаёт и возвращает список y*x"""
    list_xy = []
    for i in range(len(list_x)):
        list_xy.append(list_x[i]*list_y[i])

    list_mean.append(mean(list_xy))
    return list_xy

def create_list_square(list_values: list, list_mean: list):
    """Создаёт и возвращает список значений в степени"""
    list_values_square = []
    for i in list_values:
        list_values_square.append(i**2)

    list_mean.append(mean(list_values_square))
    return list_values_square


