# importing needed libraries
import pyotp
from flask import Flask, render_template, request
# from flask_bootstrap import Bootstrap

# configuring flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = "APP_SECRET_KEY"
# Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

# homepage route
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def generate_2fa():
    # getting form data
    secret = request.form.get("txtsecret")
    # return redirect(url_for("index"))
    secret_no_space = secret.replace(" ", "")
    result = ""
    print(secret)
    if secret_no_space:
        try:
            totp = pyotp.TOTP(secret_no_space)
            result = totp.now()
        except Exception:
            result = "Invalid code"
    return render_template('index.html', secret=secret, result=result)

# running flask server
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)
