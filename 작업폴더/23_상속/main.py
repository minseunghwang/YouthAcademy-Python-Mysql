# 상속
# 다수의 클래스를 작성할 때 중복되는 부분이 있다면 중복되는 부분을 가지고 있는 클래스를 만들어주고, 이를 상속받게 할 수 있다

# 코드의 중복을 최소화
# 기존의 클래스는 그대로 유지한 채 새로운 기능을 추가하거나 새로운 클래스를 만들어 사용

# 클래스들이 가지고 있는 공통부분을 구현한 클래스
class Animal:

    def __init__(self, name):
        print('Animal의 init')
        self.name = name

    def run(self):
        print(f'{self.name} 이(가) 달립니다.')

    def eat(self):
        print(f'{self.name} 이(가) 먹습니다.')


# Animal 클래스 상속(상속 해주는쪽(Animal : 부모), 상속 받는쪽(Dog, Cat) 자식)
class Dog(Animal):

    def __init__(self):
        # 객체가 생성될떄 자동으로 호출되는 init에서 부모 클래스의 init을 호출한다.
        # 이때 자동으로 호출될 때는 아무 값을 넘겨주지 않기 때문에 부모의 init에 매개변수가 정의되어 있다면 명시적으로 호출해주어야 한다.
        super(Dog, self).__init__('강아지')        # super(자식클래스타입, 객체주소값).__init__
        print('Dog의 init')

    def bark(self):
        print('짖습니다.')


class Cat(Animal):

    def __init__(self):
        super(Cat, self).__init__('고양이')

    def in_box(self):
        print('상자에 드갑니다.')


a1 = Dog()
a2 = Cat()

a1.run()
a1.eat()
a1.bark()

a2.run()
a2.eat()
a2.in_box()

class Rabbit(Animal):

    def __init__(self):
        super(Rabbit, self).__init__('토끼')
        # super.__init__('토끼')

    def sleep(self):
        print('잠을 잡니다')

a3 = Rabbit()
a3.run()
a3.eat()
a3.sleep()
