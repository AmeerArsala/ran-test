import ran


def _hidden_function():
    print("You can't find me!!!")


@ran.expose
def greet():
    _hidden_function()
    print("I just exposed that function!!! Lol")
