from flask import Flask, render_template

# @.1
# template 폴더 생략. template을 생략하면 render_template 함수를 통해 html파일을 지정했을때 templates 폴더에서 파일을 찾는다.
# app = Flask(__name__)

# @.2
# template_folder를 지정해주면 templates가 아닌 지정된 폴더에서 html파일을 찾는다.
app = Flask(__name__, template_folder='views')

@app.route('/')
def index():
    # return 'Hello World'
    # return '<h1>Hello World</h1><h3>flask</h3>'
    # return '''
    #             <html>
    #                 <head>
    #                     <title>이거슨제목이다</title>
    #                 </head>
    #                 <body>
    #                     <h1>하이</h1>
    #                     <h3>Flask</h3>
    #                 </body>
    #             </html>
    # '''

    # html 파일에서 데이터를 읽어온다.
    html = render_template('index.html')
    return html


app.run(host='0.0.0.0', port=80, debug=True)