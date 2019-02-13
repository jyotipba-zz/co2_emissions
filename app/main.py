from flask import Flask, render_template, flash, url_for, jsonify, request
from forms import SearchForm
import pygal
import os
from utils import get_co2_data


app = Flask(__name__)
app.config['SECRET_KEY']= os.environ.get('SECRET_KEY') or 'hard-to-guess'


@app.route("/", methods=['GET', 'POST'])
def home():
    form = SearchForm()
    return render_template ("home.html", form = form )

@app.route("/graph",methods=[ 'POST','GET'])
def draw_graph():
    #form = SearchForm()
    #country = form.country_name.data
    if request.method=="POST":
        country =  request.form['country_name']
        co2, year = get_co2_data(country)
        line_chart = pygal.Line()
        line_chart.title = 'Carbon emission for ' + country
        line_chart.x_labels = year
        line_chart.add("co2 emmison", co2)
        graph_data = line_chart.render_data_uri()
        return render_template("graph.html", graph_data = graph_data)

    return jsonify({"STATUS" : "NOT SUCCESS"})



if __name__ == '__main__':
    app.run()
