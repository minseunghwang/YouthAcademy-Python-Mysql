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


