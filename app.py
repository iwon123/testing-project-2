import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("postgresql://postgres:postgres@localhost:5432/Canadian_Stats")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Stats = Base.classes

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/canada_labour_market/wages<br/>"
        f"/canada_labour_market/cpi_Canada<br/>"
        f"/canada_labour_market/cpi_Provincial<br/>"
        f"/canada_labour_market/employement_data_Canada<br/>"
        f"/canada_labour_market/gini_index_Canada<br/>"
        f"/canada_labour_market/gini_index_Provincial<br/>"
        f"/canada_labour_market/population_per_Provincial_bothsexes<br/>"
        f"/canada_labour_market/population_per_Provincial_female<br/>"
        f"/canada_labour_market/population_per_Provincial_male<br/>"
        f"/canada_labour_market/tax_revenue_Canada<br/>"
        f"/canada_labour_market/tax_revenue_Provincial<br/>"
        f"/canada_labour_market/unemployment_Canada<br/>"
        f"/canada_labour_market/unemployment_per_Provincial<br/>"
        f"/canada_labour_market/wages_Canada<br/>"
    )


@app.route('/canada_labour_market/wages')
def wages():
    results = pd.read_sql('SELECT * FROM wages', engine)

    # Convert data into Json
    return jsonify(results.to_dict(orient = 'records'))

@app.route('/canada_labour_market/cpi_Canada')
def cpi_Canada():
    results = pd.read_sql('SELECT * FROM cpicanada', engine)

    # Convert data into Json
    return jsonify(results.to_dict(orient = 'records'))

@app.route('/canada_labour_market/cpi_Provincial')
def cpi_Provincial():
    results = pd.read_sql('SELECT * FROM cpiprovincial', engine)

    # Convert data into Json
    return jsonify(results.to_dict(orient = 'records'))

@app.route('/canada_labour_market/employement_data_Canada')
def employement_data_Canada():
    results = pd.read_sql('SELECT * FROM employmentdata', engine)

    # Convert data into Json
    return jsonify(results.to_dict(orient = 'records'))

@app.route('/canada_labour_market/gini_index_Canada')
def gini_index_Canada():
    results = pd.read_sql('SELECT * FROM giniindexcanada', engine)

    # Convert data into Json
    return jsonify(results.to_dict(orient = 'records'))

@app.route('/canada_labour_market/gini_index_Provincial')
def gini_index_Provincial():
    results = pd.read_sql('SELECT * FROM giniindexprovincial', engine)

    # Convert data into Json
    return jsonify(results.to_dict(orient = 'records'))

@app.route('/canada_labour_market/population_per_Provincial_bothsexes')
def population_per_Provincial_bothsexes():
    results = pd.read_sql('SELECT * FROM populationperprovbothsex', engine)

    # Convert data into Json
    return jsonify(results.to_dict(orient = 'records'))

@app.route('/canada_labour_market/population_per_Provincial_female')
def population_per_Provincial_female():
    results = pd.read_sql('SELECT * FROM populationperprovfemale', engine)

    # Convert data into Json
    return jsonify(results.to_dict(orient = 'records'))

@app.route('/canada_labour_market/population_per_Provincial_male')
def population_per_Provincial_male():
    results = pd.read_sql('SELECT * FROM populationperprovmale', engine)

    # Convert data into Json
    return jsonify(results.to_dict(orient = 'records'))

@app.route('/canada_labour_market/tax_revenue_Canada')
def tax_revenue_Canada():
    results = pd.read_sql('SELECT * FROM taxrevenuecanada', engine)

    # Convert data into Json
    return jsonify(results.to_dict(orient = 'records'))

@app.route('/canada_labour_market/tax_revenue_Provincial')
def tax_revenue_Provincial():
    results = pd.read_sql('SELECT * FROM taxrevenueprovincial', engine)

    # Convert data into Json
    return jsonify(results.to_dict(orient = 'records'))

@app.route('/canada_labour_market/unemployment_Canada')
def unemployment_Canada():
    results = pd.read_sql('SELECT * FROM unemploymentcanada', engine)

    # Convert data into Json
    return jsonify(results.to_dict(orient = 'records'))

@app.route('/canada_labour_market/unemployment_per_Provincial')
def unemployment_per_Provincial():
    results = pd.read_sql('SELECT * FROM unemploymentperprov', engine)

    # Convert data into Json
    return jsonify(results.to_dict(orient = 'records'))

if __name__ == '__main__':
    app.run(debug=True)
