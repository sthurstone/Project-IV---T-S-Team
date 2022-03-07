from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('Index.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Analytics')
def Analytics():
    return render_template('Analytics.html')

@app.route('/Survey')
def Survey():
    return render_template('Survey.html')

if __name__=='__main__':
    app.run(debug=True)