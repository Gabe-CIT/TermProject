from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("testforgot.html") #Change name of .html to whatever you test(insertname).html to test templates

if __name__ == "__main__":
    app.run(debug=True)