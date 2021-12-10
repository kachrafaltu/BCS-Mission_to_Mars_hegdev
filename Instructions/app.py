# web scraping main app code
from flask import Flask, render_template,redirect
import pymongo
import scrape_mars

app = Flask(__name__)

# setup mongo connection

# connect to mongo db and collection
# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)
    db = client.mars_data
    # Find one record of data from the mongo database
    basic_data= db.mars_basic_data.find_one()
    print("--------In route/ ----")
    print("In home",basic_data)
    hemis_data = db.hemis.find()
    # Return template and data
    return render_template("index.html", mars_basic_info=basic_data)

@app.route("/scrape")
def scraper():
    # call python file to upload the data to the inventory
    mars_data=scrape_mars.scrape()
    # write a statement that finds all the items in the db and sets it to a variable
#    mars_hemis = list(hemis.find())
#    print(hemis)

    # render an index.html template and pass it the data you retrieved from the database
#    return render_template("index.html", hemis=hemis)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)