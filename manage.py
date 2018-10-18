from flask_script import Manager

from astrahus import application

manager = Manager(application)

@manager.command
def hello():
    print("hello")

if __name__ == "__main__":
    manager.run()
