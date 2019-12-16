class Horse:

    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def move(self, vector_x, vector_y):
        if 1 <= abs(vector_x) <= 2 and 1 <= abs(vector_y) <= 2 and abs(vector_x) != abs(vector_y):
            self.__x += vector_x
            self.__y += vector_y
        else:
            raise Exception("Invalid Coords")

    def moveY(self, direction):
        '''
        Смещение на 2 клетки по оси Y
        :param direction:
        :return: list of coords
        '''
        self.__x += 2
        self.__y += 1
        coords  = ((self.__x, self.__y), (self.__x - 2, self.__y + 1))
        self.__x, self.__y = coords[1]
        return coords

    def moveX(self):
        pass

    @property
    def pos_x(self):
        return self.__x

    @property
    def pos_y(self):
        return self.__y