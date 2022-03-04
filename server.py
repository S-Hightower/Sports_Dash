from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/premier')
def premier():
    return render_template('premier.html')

@app.route('/laliga')
def laliga():
    return render_template('laliga.html')

@app.route('/ligueone')
def ligueone():
    return render_template('ligueone.html')

@app.route('/brasil')
def brasil():
    return render_template('brasil.html')

@app.route('/mls')
def mls():
    return render_template('mls.html')

@app.route('/bundesliga')
def bundesliga():
    return render_template('bundesliga.html')

@app.route('/italia')
def italia():
    return render_template('italia.html')

@app.route('/eredivisie')
def eredivisie():
    return render_template('eredivisie.html')

@app.route('/argentina')
def argentina():
    return render_template('argentina.html')

@app.route('/mexico')
def mexico():
    return render_template('mexico.html')

if __name__=='__main__':
    app.run(debug=True)