from flask import Flask, render_template, request, redirect

app = Flask(__name__)

dogs = [
    {
        'name': 'Fido',
        'breed': 'Golden Retriever',
        'age': 5
    },
    {
        'name': 'Rex',
        'breed': 'German Shepherd',
        'age': 3
    },
    {
        'name': 'Spot',
        'breed': 'Dalmatian',
        'age': 2
    }
]

# Define the route for the homepage
@app.route('/')
def index():
    # Render the index.html template and pass in the list of dogs as a variable
    return render_template('index.html', dogs=dogs)

@app.route('/add_dog')
def add_dog():
    return render_template('add_dog.html')

# Define the route for the form submission
@app.route('/submit_dog', methods=['POST'])
def submit_dog():
    # Get the name, breed, and age of the dog from the form submission
    name = request.form['name']
    breed = request.form['breed']
    age = request.form['age']
    # Append the dog to the list of dogs
    dogs.append({
        'name': name,
        'breed': breed,
        'age': age
    })
    # Redirect to the homepage
    return redirect('/')

app.run(debug=True, port=5500)