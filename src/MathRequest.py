class MathRequest:

    def __init__ (self, ope1, operator, ope2):
        self.ope1 = ope1
        self.operator = operator
        self.ope2 = ope2
        self.res = None

    def get_ope1(self):
        return self.ope1

    def get_operator(self):
        return self.operator

    def get_ope2(self):
        return self.ope2

    def get_res(self):
        return self.res

    def set_res(self, value):
        self.res = value

    def to_string(self):
        return (str(self.ope1) + " " + self.operator + " " +
                str(self.ope2) + " = " + str(self.res))