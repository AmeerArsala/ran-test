def another_hidden_function():
    print("I don't want to be exposed to RAN")


@ran.expose
def show_me():
    print("Please show me!")
