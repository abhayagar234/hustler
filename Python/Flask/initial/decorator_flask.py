from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"{function()}"

    return wrapper


class Make:
    def emphasis(self, function):
        def wrapper():
            return f"{function()}"

        return wrapper

    def underlined(self, function):
        def wrapper():
            return f"<u>{function()}</u>"

        return wrapper


m = Make()


@app.route("/")
@make_bold
@m.emphasis
@m.underlined
def hello():
    return "hello guest"


@app.route("/users/<path:name>/<int:number>")
def greeting(name, number):
    return f"hello there {name}, you are {number} years old."


if __name__ == "__main__":
    app.run(debug=True)
