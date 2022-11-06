from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port="9999", debug=True)
    app.run(host="0.0.0.0", port="9999", debug=False)
    # app.run(host='192.168.0.58', port='9000', debug=False)