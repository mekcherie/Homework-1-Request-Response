
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Hey World!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked, {users_dessert} ?'


@app.route('/madlibs/<adjective>/<noun>')
def any_word(adjective, noun):
    return f'How many times can you subtract 10 from 100?  {adjective} Once {noun}?...{noun} The next time you would be subtracting 10 from 90.'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):

    number1 = int(number1) 
    number2 = int(number2)

    answer = number1 * number2 
    return f' {number1} multiply {number2} is {answer}'












if __name__ == '__main__':
    app.run(debug=True)
