import sqlite3
import pandas as pd
from pandas import DataFrame
from plane_sweep import *
from brute_force import *
from divide_conquer import *
import plotly.express as px

class Database:

	def __init__(self):
		self.connection = sqlite3.connect('SmartphonesDB.db')
		self.cursor = self.connection.cursor()
		self.db = pd.read_csv('db/smartphones.csv', delimiter=';')

	"""
	gets input from user, returns graph with skyline points
	"""
	def get_skyline(self, column1, column2, minmax, method):
		items = self.pick_columns(column1, column2)
		skyline_points = self.skyline_method(method, items, minmax)
		not_skyline_points = self.not_skyline(items, skyline_points)
		return self.graph(skyline_points, not_skyline_points)

	"""
	select skyline points by method picked by the user
	"""
	def skyline_method(self, method, items, minmax):
		if str(method) == 'plane_sweep':
			return plane_sweep(items, minmax)
		elif str(method) == 'brute_force':
			return brute_force(items, minmax)
		else:
			return divide_conquer(items, minmax)

	"""
	generate plotly graph with prepared divided points
	skyline == points laying on skyline
	other == points not laying on skyline
	"""
	def graph(self, skyline, other):
		skylinen = [i.name for i in skyline]
		notskylinen = [j.name for j in other]
		sky_df = self.db.loc[self.db['Name'].isin(skylinen)]
		nsky_df = self.db.loc[self.db['Name'].isin(notskylinen)]
		sky_df = sky_df.sort_values(by=[str(skyline[0].x_name)])
		fig = px.line(sky_df, x=str(skyline[0].x_name), y=str(skyline[0].y_name), hover_data=self.get_columns())
		fig.update_traces(mode='markers+lines')
		fig2 = px.scatter(nsky_df, x=str(other[0].x_name), y=str(other[0].y_name), hover_data=self.get_columns())
		fig.add_trace(fig2.data[0])
		return fig

	"""
	select points not on skyline
	"""
	def not_skyline(self, items, skyline):
		others = []
		for point in items:
			if point not in skyline:
				others.append(point)
		return others

	"""
	returns SkylineParam list with x = column1 and y = column2
	"""
	def pick_columns(self, column1, column2):
		items = []
		for index, row in self.db.iterrows():
			new_item = SkylineParam()
			new_item.name = row[0]
			new_item.x = row[str(column1)]
			new_item.y = row[str(column2)]
			new_item.x_name=str(column1)
			new_item.y_name=str(column2)
			items.append(new_item)
		return items

	def get_columns(self):
		self.cursor.execute('SELECT * FROM SMARTPHONES')
		return [d[0] for d in self.cursor.description]

	def get_names(self, points):
		names = []
		for point in points:
			names.append(point.name)
		return names

	def get_points(self, points):
		coords = []
		for point in points:
			c = [point.x, point.y]
			coords.append(c)
		return coords

"""
reprezenting 1 point on a 2D graph
"""
class SkylineParam:
	def __init__(self):
		self.name = ""
		self.x = 0
		self.y = 0
		self.x_name=""
		self.y_name=""