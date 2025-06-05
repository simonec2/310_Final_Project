import functions

from flask import Flask, render_template, request

# Create an instance of Flask
app = Flask(__name__)

# Create a view function for /
@app.route('/')
def index():
    return render_template('index.html')
# Create a view function for /results
@app.route('/results', methods=["GET", "POST"])
def results():
    if request.method == "POST":
        #  call wikipedia_locationsearch() and then render the template results.html with the results returned by the function.
        # Note that everything in the forms data dictionary comes as a string, so you will need
        # to convert the max_result and radius data from string to int and float with the int() and float() functions.

        place = request.form["place"]
        max_results = int(request.form["max_results"])
        radius = float(request.form["radius"])
        if "sort" in request.form:
            sort = True
        else:
            sort = False
        results = functions.wikipedia_locationsearch(place, max_results, radius, sort)

        return render_template('results.html', results=results, place=place)
    else:
        # should return an HTTP 400 error with a “Wrong HTTP method” message
        # (this does not need to be styled or be a fully-formed HTML page).
        return "Wrong HTTP method", 400
