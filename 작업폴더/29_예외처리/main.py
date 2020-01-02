# 예외 : 프로그램에서 실행 중 발생되고 예측이 가능하며 대처가 가능한 오류

# 예외가 발생하게 되면 개발자가 만든 프로그램을 강제 종료시킨다.

# 예외 발생시 프로그램 수행을 중단하고 대비한 코드를 동작시킬 수 있도록 하는 것을 예외 처리라고 한다.

# try : 정상적으로 수행되어야 할 코드
# except : try 부분에서 예외가 발생했을 경우 동작해야할 코드
# try 부분의 코드가 수행되다 예외가 발생하면 try 부분은 더 이상 수행하지 않고, except 부분으로 이동한다.
# 예외처리를 하게 되면 오류 발생시 개발자가 대처를 했다고 판단해 프로그램을 중단시키지 않는다.
try :
    # a1 = 10 / 2
    a1 = 10 / 0
    print(f'a1 : {a1}')
except :
    print('예외발생')

print('이 부분이 수행될까요 ?')

print('------------------------')

# 발생되는 예외 별로 처리하기

try :
    a1 = 10 / 0
    list1 = [10, 20, 30]
    print(list1[10])

    class TestClass1()  :
        pass

    t1 = TestClass1()
    t1.f1()

except ZeroDivisionError as e:
    print('0으로 나누기를 하는 수학적 오류가 발생했습니다.')
    print(e)
except IndexError as e:
    print('리스트의 인덱스 범위를 벗어났습니다.')
    print(e)
except Exception as e:
    print('그 외의 오류 발생')
    print(e)

print('이 부분이 수행될뀨?')         # 예외처리를 하게되면 try 부분만 중단되기 때문에 다른 코드는 실행된다. (이 부분은 출력된다)
