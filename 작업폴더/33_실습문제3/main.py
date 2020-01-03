# 두 수를 객체 생성할 때 입력받아 사칙연산 결과를 반환하는 클래스를 설계하세요.

# 클래스명 : simplecalc
# 메서드명 : add, sub, mul, div

class simplecalc():

    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a//b

calc = simplecalc()
print(calc.add(10,2))
print(calc.sub(10,2))
print(calc.mul(10,2))
print(calc.div(10,2))


class simplecalc2:
    def __init__(self, a1, a2):
        self.number1 = a1
        self.number2 = a2

    def add(self):
        return self.number1 + self.number2

    def sub(self):
        return self.number1 - self.number2

    def mul(self):
        return self.number1 * self.number2

    def div(self):
        return self.number1 // self.number2

calc = simplecalc2(100,200)
r1 = calc.add()
r2 = calc.sub()
r3 = calc.mul()
r4 = calc.div()

print(f'더하기 : {r1}')
print(f'빼기 : {r2}')
print(f'곱하기 : {r3}')
print(f'나누기 : {r4}')