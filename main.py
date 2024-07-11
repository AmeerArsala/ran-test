import ran


@ran.expose
def greet(num: int, text: str):
    print("Hello World")


def _hidden_function():
    print("I'm hidden!")
