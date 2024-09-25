from list_command import *


list_y = [77923.0, 46044.3, 1792048.2, 288951.6, 715050.4, 1000247.6, 538340.2, 52167.8, 118134.7, 69195.3, 126827.2, 141294.8, 541188.0]
list_x = [201, 147, 2613, 532, 1316, 2142, 1325, 212, 436, 227, 340, 633, 1372]

class Econom:

    def __init__(self, y: list, x: list):
        self.list_y = y
        self.list_x = x
        self.list_mean = create_list_mean(y, x)
        self.list_sum = create_list_sum(y, x)
        self.list_xy = create_list_xy(x, y, self.list_mean, self.list_sum)
        self.list_x_square = create_list_square(x, self.list_mean, self.list_sum)
        self.list_y_square = create_list_square(y, self.list_mean, self.list_sum)
        self.b = None
        self.a = None
        Econom.table_analysis(self)

        self.list_Yx = create_Yx(self, self.list_mean, self.list_sum)
        self.list_y_Yx_square = create_list_y_Yx_square(self, self.list_mean, self.list_sum)

    def table_analysis(self):
        self.b = create_regress_coeff(self)
        self.a = create_konst(self)

    def __repr__(self):
        return (
            f"Список средних значений: {self.list_mean}\n"
            f"Список сумм значений: {self.list_sum}\n"
            f"Список y: {self.list_y}\n"
            f"Список x: {self.list_x}\n"
            f"Список x*y: {self.list_xy}\n"
            f"Список x^2: {self.list_x_square}\n"
            f"Список y^2: {self.list_y_square}\n"
            f"Список Yx: {self.list_Yx}\n"
            f"Список y-Yx: {self.list_y_Yx_square}\n"
            
            
            "\n"
            f"Значение b: {self.b}\n"
            f"Значение a: {self.a}\n"
        )


x_y = Econom(list_y, list_x)
print(x_y)
