import ran


@ran.expose
def greet():
    print("Hello World")


def _hidden_function():
    print("I'm hidden!")
