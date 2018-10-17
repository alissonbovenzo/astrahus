from flask import Flask, render_template

application = Flask(__name__)


def config(app: Flask):
    app.config.from_mapping(
        SECRET_KEY='Astrahus',
        URI_MONGO='mongodb://develop:develop1@ds247170.mlab.com:47170/astrahus'
    )

@application.route("/")
def home_page():
    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html",
        online_users=online_users)


if __name__ == '__main__':
    config(application)
    application.run(host='0.0.0.0')
