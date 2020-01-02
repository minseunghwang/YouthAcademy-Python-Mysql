# 파일 입출력

# w : 쓰기. 기존 내용이 있으면 덮어 씌운다. 파일이 없으면 새로 만든다.
# a : 쓰기. 기존 내용이 있으면 이어서 쓴다. 파일이 없으면 새로 만든다.
# r : 읽기. 파일이 없으면 오류 발생

# t : 문자열 -> 텍스트 파일
# b : 모든 데이터(정수, 실수, 문자열, 리스트, 객체 등등....) -> 데이터 파일


a1 = 100
a2 = 11.11
a3 = True

# 기본 파일 읽고 쓰기
def write_to_file1():
    # fp = open('test1.txt', 'wt', encoding='utf-8')        # 이렇게 하면 맨 마지막에 fp.close() 통해서 반드시 닫아줘야 하지만

    ## with 문을 사용하게 되면 자동으로 닫힌다. (맨 마지막에 fp.close() 안해줘도 됌)
    with open('test1.txt', 'wt', encoding='utf-8') as fp :
        fp.write('안녕하세요\n')
        fp.write(f'{a1}\n')
        fp.write(f'{a2}\n')
        fp.write(f'{a3}\n')

    # fp.close()
    
    print('파일 쓰기 완료')

def read_from_file1():

    with open('test1.txt', 'rt', encoding='utf-8') as fp:
        # 한줄 씩 읽어온다.
        # a1 = fp.readline()
        # a2 = fp.readline()
        # a3 = fp.readline()
        # a4 = fp.readline()
        # 라인단위로 모두 읽어와 리스트에 담아 저장한다.
        str_list = fp.readlines()

    # print(f'a1 : {a1}')
    # print(f'a2 : {a2}')
    # print(f'a3 : {a3}')
    # print(f'a4 : {a4}')
    print(str_list)

# pickle : 다양한 타입의 데이터를 읽고 쓸 수 있도록 기능을 제공하는 모델 (우리가 열어서 볼라고 하는건 아님. 알아볼수 읎다)
import pickle

# 객체를 읽어서 사용할때 주의할 점
# 사용하는 곳에 클래스가 작성되어 있는 모듈이 있어야 한다.
class TestClass :
    def __init__(self):
        self.a1 = 100
        self.a2 = 200

    def test_method1(self):
        print('test_method1 호출')

def write_to_file2():
    with open('test2.txt', 'wb') as fp :
        pickle.dump(100, fp)
        pickle.dump(11.11, fp)
        pickle.dump(True, fp)
        pickle.dump('인녕하세요', fp)
        pickle.dump([1,2,3], fp)
        pickle.dump((1,2,3), fp)
        pickle.dump({'a1' : 100, 'a2' : 200}, fp)
        t1 = TestClass()
        pickle.dump(t1, fp)
        
    print('쓰기완료')

def read_from_file2():
    with open('test2.txt', 'rb') as fp:
        a1 = pickle.load(fp)
        a2 = pickle.load(fp)
        a3 = pickle.load(fp)
        a4 = pickle.load(fp)
        a5 = pickle.load(fp)
        a6 = pickle.load(fp)
        a7 = pickle.load(fp)
        a8 = pickle.load(fp)

    print(f'a1 : {a1}')
    print(f'a2 : {a2}')
    print(f'a3 : {a3}')
    print(f'a4 : {a4}')
    print(f'a5 : {a5}')
    print(f'a6 : {a6}')
    print(f'a7 : {a7}')
    print(f'a8.a1 : {a8.a1}')
    print(f'a8.a2 : {a8.a2}')


write_to_file1()
print('-------')
read_from_file1()
print('*******')
write_to_file2()
print('^^^^^^^')
read_from_file2()