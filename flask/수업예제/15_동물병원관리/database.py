import pymysql

def get_connection():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='flaskdb1', charset='utf8')
    return conn

# 동물 정보 저장하는 함수
def add_animal_info(animal_type, animal_name, animal_age, animal_weight):

    conn = get_connection()

    sql = '''
            insert into animal_table(animal_type, animal_name, animal_age, animal_weight)
            values(%s, %s, %s, %s)
        '''

    cursor = conn.cursor()
    cursor.execute(sql, (animal_type, animal_name, animal_age, animal_weight))

    conn.commit()
    conn.close()


# 동물 정보 검색하는 함수
def get_search_info(animal_name):

    conn = get_connection()

    sql = '''
            select animal_type, animal_name, animal_age, animal_weight
            from animal_table
            where animal_name = %s
    '''

    cursor = conn.cursor()
    cursor.execute(sql, animal_name)

    result = cursor.fetchall()

    animal_list = []

    for row in result:
        animal_dict ={
            'animal_type' : row[0],
            'animal_name' : row[1],
            'animal_age' : row[2],
            'animal_weight' : row[3],
        }
        animal_list.append(animal_dict)

    conn.close()
    return animal_list

# 동물 전체 데이터를 구하는 함수
def get_total_info():

    conn = get_connection()

    sql = '''
            SELECT animal_type, count(*) FROM flaskdb1.animal_table GROUP BY animal_type;
            '''

    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    animal_list = []
    sum = 0
    for row in result:
        sum += row[1]
        total_dict ={
            'animal_type' : row[0],
            'animal_count' : row[1],
        }
        animal_list.append(total_dict)

    conn.close()
    return (animal_list,sum)