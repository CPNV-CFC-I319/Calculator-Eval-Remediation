class MathLib:

    @classmethod
    def execute(cls, math_request):
        operator = math_request.get_operator()
        ope1 = math_request.get_ope1()
        ope2 = math_request.get_ope2()

        match operator:
            case 'add':
                math_request.set_res(ope1 + ope2)
            case 'sub':
                math_request.set_res(ope1 - ope2)
            case 'mul':
                math_request.set_res(ope1 * ope2)
            case 'div':
                math_request.set_res(ope1 / ope2)
            case 'mod':
                math_request.set_res(ope1 % ope2)
            case 'pow':
                math_request.set_res(ope1 ** ope2)
            case 'root':
                math_request.set_res(cls.__root(ope1, ope2))
            case 'root':
                math_request.set_res(cls.__root(ope1, ope2))
            case _:
                raise OperatorNotSupportedException

    @staticmethod
    def __root(ope1, ope2):
        return round((ope1 ** (1.0 / ope2)), 2)

class MathLibException(Exception):
    pass

class OperatorNotSupportedException(MathLibException):
    pass