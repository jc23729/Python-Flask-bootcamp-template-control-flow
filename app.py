# from flask import Flask, render_template

# app = Flask(__name__)


# """
# >With Jinja templating we can pass variables using {{ variable }} syntax
# >We also have aceess to control flow syntax in our templates such as FOR LOOPS and IF Statements
# >they use a {% %}syntax
# >Imagine you passed a list variable to the HTML using template variables
# >Instead of displaying the entire list at once, we can display each item in the python list as a bulleted HTML list
# > {% %}= control flow logic
# > {{}} = variable 
# Example.........
# <ul>
#         {% for item in mylist %}
#         <li> {{ item }}</li>
#         {% endfor %}
# </ul>
# """
# @app.route('/')
# def index():
#     puppies = ['Fluffy', 'Rufus', 'Spike']
#     return render_template('basic.html', puppies= puppies)#you have parameter mylist and setting it equal to mylist with [1,2,3,4,5,6]
#     #that mylist needs to match with the html file you created.


# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('puppy.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)