from flask import render_template
from flask_app import app

@app.route('/')
def main():
    return render_template('test.html')

if __name__=="__main__":
    app.run(debug=True)