from flask import Flask , render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')

# request.args.get("")

@app.route('/')
def main():
    """ 메인 페이지 """
    return render_template("main.html")

@app.route('/test')
def test_page():
    """ 테스트 페이지 """
    return render_template("test.html")

@app.route('/result')
def result_page():
    """ 결과 페이지 """
    return render_template("result.html")

@app.route('/hospital')
def hospital_map():
    """ 병원 추천 페이지 """
    return render_template("hospital.hml")

@app.errorhandler(404)
def page_not_found(error):
    ''' 404 페이지 처리 '''
    return render_template("not_found_404.html"),404
