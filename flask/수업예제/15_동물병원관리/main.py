from flask import Flask, render_template, request
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    html = render_template('index.html')
    return html

@app.route('/animal_info_add')
def animal_info_add():
    html = render_template('animal_info_add.html')
    return html

@app.route('/animal_info_add_pro', methods=['post'])
def animal_info_add_pro():

    animal_type = request.values.get('animal_type')
    animal_name = request.values.get('animal_name')
    animal_age = request.values.get('animal_age')
    animal_weight = request.values.get('animal_weight')

    animal_info = {
        'animal_type' : animal_type,
        'animal_name' : animal_name,
        'animal_age' : animal_age,
        'animal_weight' : animal_weight,
    }

    db.add_animal_info(animal_type, animal_name, animal_age, animal_weight)

    html = render_template('animal_info_add_pro.html', animal_info=animal_info)
    return html

@app.route('/animal_info_search')
def animal_info_search():

    html = render_template('animal_info_search.html')
    return html

@app.route('/search_info_result', methods=['post'])
def search_info_result():
    animal_name = request.values.get('animal_name')

    animal_list = db.get_search_info(animal_name)

    html = render_template('search_info_result.html', animal_list=animal_list)
    return html

@app.route('/animal_info_total')
def animal_info_total():

    result = db.get_total_info()
    total_info = result[0]
    all_count = result[1]

    html = render_template('animal_info_total.html', total_info=total_info, all_count=all_count)
    return html

@app.route('/all_of_animal')
def all_of_animal():

    animal_list = db.all_animal_list()

    html = render_template('all_of_animal.html', animal_list = animal_list)
    return html




app.run(host='0.0.0.0', port=80, debug=True)

# kk : [{'animal_type': 'dog', 'animal_name': '김초롱', 'animal_age': 15, 'animal_weight': 7}]
# animal_list :  [{'animal_pk': 1, 'animal_type': 'dog', 'animal_name': '김초롱', 'animal_age': 15, 'animal_weight': 7}, {'animal_pk': 2, 'animal_type': 'cat', 'animal_name': '김냥냥', 'animal_age': 10, 'animal_weight': 9}, {'animal_pk': 3, 'animal_type': 'dog', 'animal_name': '강아쥐', 'animal_age': 11, 'animal_weight': 11}, {'animal_pk': 4, 'animal_type': 'dog', 'animal_name': '강아쥐', 'animal_age': 11, 'animal_weight': 11}, {'animal_pk': 5, 'animal_type': 'dog', 'animal_name': '강아쥐', 'animal_age': 11, 'animal_weight': 11}, {'animal_pk': 6, 'animal_type': 'bird', 'animal_name': '짭새', 'animal_age': 11, 'animal_weight': 23}, {'animal_pk': 7, 'animal_type': 'dog', 'animal_name': '강하지', 'animal_age': 3, 'animal_weight': 10}, {'animal_pk': 8, 'animal_type': 'bird', 'animal_name': '피존', 'animal_age': 10, 'animal_weight': 20}, {'animal_pk': 9, 'animal_type': 'cat', 'animal_name': '샥스핀', 'animal_age': 6, 'animal_weight': 17}]
