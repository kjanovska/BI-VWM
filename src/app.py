from flask import Flask, render_template, request, redirect, url_for, session
from database import *
import dash
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = Flask(__name__)
app.config.from_pyfile('config/config.py')

@app.route("/", methods=['GET', 'POST'])
def index():
	db = Database()
	if request.method == "POST":
		column1 = request.form.get('attr1')
		column2 = request.form.get('attr2')
		c1minmax = request.form.get('attr3')
		c2minmax = request.form.get('attr4')
		method = request.form.get('attr5')
		if request.form['submit_button'] == 'make_graph':
			return render_dashboard([column1, column2, c1minmax, c2minmax, method])
		elif request.form['submit_button'] == 'make_table':
			return render_datatable()
	return render_template('index.html')

@app.route('/d')
def render_dashboard(params):
	session['column1'] = params[0]
	session['column2'] = params[1]
	session['c1minmax'] = params[2]
	session['c2minmax'] = params[3]
	session['method'] = params[4]
	return redirect('/dashboard/')

"""
dashboard for skyline graphs
"""
dashboard = dash.Dash(__name__, server=app, url_base_pathname='/dashboard/')
dashboard.layout = html.Div(children=[
	html.H3(children='Skyline graph', style={'textAlign': 'center'}),
    dcc.Graph(
        id='graph'
    ),
    html.A(html.Button('Back', className='buttonback', id="buttonback"),
    href='/'),
    html.Div(id='divid')
])

application = DispatcherMiddleware(app, {
	'/dashboard/': dashboard.server
	})

@dashboard.callback(
	Output(component_id='graph', component_property='figure'),
	[
		Input(component_id='divid', component_property='children')
	]
	)
def gen_graph(value):
	db = Database()
	column1 = session.get('column1', None)
	column2 = session.get('column2', None)
	c1minmax = session.get('c1minmax', None)
	c2minmax = session.get('c2minmax', None)
	method = session.get('method', None)
	graph = db.get_skyline(column1, column2, [c1minmax, c2minmax], method)
	return graph


@app.route('/t')
def render_datatable():
	return redirect('/datatable/')

"""
dashboard for table showing the entire database
"""
db = Database()
df = pd.DataFrame(db.db)
datatable = dash.Dash(__name__, server=app, url_base_pathname='/datatable/')
datatable.layout = html.Div(children=[
	html.H3(children='Database content', style={'textAlign': 'center'}),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns],
        data=df.to_dict('records'),
        sort_action="native",
        sort_mode="multi"
    ),
  html.A(html.Button('Back', className='buttonback', id="buttonback"),
    href='/'),
    html.Div(id='div2')
])

application2 = DispatcherMiddleware(app, {
	'/datatable/': datatable.server
	})

if __name__=='__main__':
	app.run(debug=True)
