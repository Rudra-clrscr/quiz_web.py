from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

answers = {
    
    'q1':'A',
    'q2':'C',
    'q3':'B'
}
@app.route('/home')
def quiz():
    return render_template('question.html')

@app.route('/result', methods=['POST'])
def result():
    score = 0
    for key, value in answers.items():
        if request.form[key] == value:
            score += 1
    return render_template('result.html', score=score)


if __name__ == '__main__':
    app.run(debug=True)