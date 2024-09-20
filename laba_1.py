from list_command import *


list_x = [201, 147, 2613, 532, 1316, 2142, 1325, 212, 436, 227, 340, 633, 1372]
list_y = [77923.0, 46044.3, 1792048.2, 288951.6, 715050.4, 1000247.6, 538340.2, 52167.8, 118134.7, 69195.3, 126827.2, 141294.8, 541188.0]

class Econom:

    def __init__(self, x: list, y: list):
        self.list_x = x
        self.list_y = y
        self.list_mean = create_list_mean(y, x)
        self.list_xy = create_list_xy(x, y, self.list_mean)
        self.list_x_square = create_list_square(x, self.list_mean)
        self.list_y_square = create_list_square(y, self.list_mean)

    def __repr__(self):
        return (
            f"Список x: {self.list_x}\n"
            f"Список y: {self.list_y}\n"
            f"Список средних значений: {self.list_mean}\n"
            f"Список x*y: {self.list_xy}\n"
            f"Список x^2: {self.list_x_square}\n"
            f"Список y^2: {self.list_y_square}\n"
        )


x_y = Econom(list_x, list_y)
print(x_y)
