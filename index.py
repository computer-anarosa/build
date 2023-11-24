from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
 
@app.route('/contatos')
def contacts():
    return render_template('contacts.html')

@app.route('/sobre')
def about():
    return render_template('about.html')

@app.route('/privacidade')
def policies():
    return render_template('policies.html')


if __name__ == '__main__':
    app.run(debug=True)