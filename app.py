import functions

from flask import Flask, render_template, request

from functions import get_recipe_data_safe, get_recipe_info_safe, update_saved_list, read_saved_list

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

        ingredients = request.form["ingredients"]
        number = int(request.form["number"])

        recipe_data = get_recipe_data_safe(ingredients, number)

        return render_template('results.html', results=recipe_data)
    else:
        # should return an HTTP 400 error with a “Wrong HTTP method” message
        # (this does not need to be styled or be a fully-formed HTML page).
        return "Wrong HTTP method", 400
@app.route('/recipe', methods=['GET', 'POST'])

def recipe():
    if request.method == "POST":
        id = None
        for key in request.form:
            if key.startswith("btn_"):
                id = key.split("_")[1]
        print(id)
        recipe_info = get_recipe_info_safe(int(id))
        return render_template("recipe.html", recipe=recipe_info)

@app.route('/saved', methods=['GET', 'POST'])

def saved():
    if request.method == "POST":
        id = None
        for key in request.form:
            if key.startswith("btn_"):
                id = key.split("_")[1]
        print(id)
        update_saved_list(id)
        recipe_info = get_recipe_info_safe(int(id))
        return render_template("saved.html", recipe=recipe_info)

@app.route('/favorited')
def favorites():
    favorites = read_saved_list()
    favorites_list = []
    for favorite in favorites:
        recipe_detail = get_recipe_info_safe(int(favorite))
        favorites_list.append(recipe_detail)
    return render_template("favorited.html", results=favorites_list)

