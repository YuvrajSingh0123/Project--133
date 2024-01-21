from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():

    name = "Yuvraj Singh"
    age = "16" 

    return render_template('index.html' , name = name , age = age)

@app.route("/father")
def father():

    name = "Brijesh Singh" 
    age = "40" 

    return render_template('father.html' , name = name , age = age)


@app.route("/mother")
def mother():

    name = "Sunita Singh" 
    age = "40" 

    return render_template('mother.html' , name = name , age = age)

@app.route("/brother")
def friend():

    name = "Krishna Singh" 
    age = "13" 

    return render_template('friend.html' , name = name , age = age)

if __name__  ==  '__main__':
    app.run(debug=True)
