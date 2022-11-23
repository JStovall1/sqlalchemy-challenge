# Import Dependencies
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import  Session
from sqlalchemy import create_engine, func      
from flask import Flask, jsonify


##Database setup
####################################################

#Create engine 
engine = create_engine('sqlite:///Resources/hawaii.sqlite')

#reflect an existing database into a new model
Base = automap_base()

#reflect the tables
Base.prepare(engine, reflect=True)

#save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station


## Flask Setup
app= Flask(__name__)

#Home Route
@app.route('/')
def home():

    """List all available routes"""
    return(
        'AVAILABLE ROUTES<br>'
        '/api/v1.0/precipitation<br>'
        'route3'
    )

    #  Precipitation Route
@app.route('/api/v1.0/precipitation')
def route2():
    # Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
    session = Session(engine)
    precip = session.query(measurement.date, measurement.prcp)
    session.close()

    # Return the JSON representation of your dictionary.
   
    rainy_days = []
        
    for date, prcp in precip:
        day_dict = {}

        day_dict['date'] = date
        day_dict['prcp'] = prcp

        rainy_days.append(day_dict)

    return jsonify(rainy_days)


    # Station Route
        # @app.route('/api/v1.0/stations')
        # def route3():
    # Query the dates and temperature observations of the most active station for the previous year of data.
    # Return a JSON list of temperature observations (TOBS) for the previous year.


    # * `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
    #  * Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.
    # * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than or equal to the start date.
    # * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates from the start date through the end date (inclusive).

if __name__ == '__main__':
    app.run(debug=True)