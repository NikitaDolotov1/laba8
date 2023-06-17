class Exception1(BaseException):
    pass

class Exception2(BaseException):
    pass

class Exception3(BaseException):
    pass

class DataTypes:
    def str(self, data):
        if not isinstance(data, str):
            raise Exception1("Необходимо написать текст")
        return print(data)

    def int(self, data):
        if not isinstance(data,int):
            raise Exception2("Необходимо написать число")
        return print(data)

    def list(self, data):
        if not isinstance(data, list):
            raise Exception3("Необходимо написать список")
        return print(data)


class FixErorr:
    def __init__(self):
        self.fix = DataTypes()

    def fixStr(self, data):
        try:
            self.fix.str(data)


        except Exception1:
            print("Введено", data, "Необходимо написать текст")

    def fixInt(self, data):
        try:
            self.fix.int(data)

        except Exception2:
            print("Введено", data, "Необходимо написать число")

    def fixList(self, data):
        try:
            self.fix.list(data)
            print(data)
        except Exception3:
            print("Введено",data, " Необходимо написать список")

f = FixErorr()

f.fixStr(1334)
f.fixInt("Привет")
f.fixList(2)
