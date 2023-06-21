# import necessary packages
from flask import Flask, jsonify
import mariadb

# establish a connection to the MariaDB
conn = mariadb.connect(
    user="your_username",  # replace with your MariaDB username
    password="your_password",  # replace with your MariaDB password
    host="localhost",  # assuming your MariaDB server is running locally
    database="flask_animals"  # the database we want to connect to
)

# create a cursor for executing SQL statements
cur = conn.cursor()

# initialize a new Flask application
app = Flask(__name__)

# define a route for getting all animals
@app.route("/animals", methods=["GET"])
def get_animals():
    cur.callproc('GetAllAnimals')  # call the stored procedure to get all animals
    result = cur.fetchall()  # fetch all rows returned by the procedure
    return jsonify(result)  # convert the result to JSON and return it

# define a route for getting all dogs
@app.route("/dogs", methods=["GET"])
def get_dogs():
    cur.callproc('GetDogs')  # call the stored procedure to get all dogs
    result = cur.fetchall()  # fetch all rows returned by the procedure
    return jsonify(result)  # convert the result to JSON and return it

# define a route for getting all cats
@app.route("/cats", methods=["GET"])
def get_cats():
    cur.callproc('GetCats')  # call the stored procedure to get all cats
    result = cur.fetchall()  # fetch all rows returned by the procedure
    return jsonify(result)  # convert the result to JSON and return it

# run the Flask application (only if this script is the main script)
if __name__ == "__main__":
    app.run(debug=True)  # run the app in debug mode
