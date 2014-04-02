"""
Data Visualization

Takes in parsed data from a CSV file and renders it onto a chart.

Copyright(c) 2014 Edward Moreno
Distributed under the Creative Commons Attribution 3.0 Unported license.
"""

from collections import Counter

import matplotlib.pyplot as plt
import numpy.numarray as na

import parse as p

def visualize_days(file_path):
	#Parse data
	self.data_file, self.headers = p.parse(file_path, ",")

	#Make a counter from each day of the week
	counter = Counter(item["DayOfWeek"] for item in self.data_file)
	#seperate counter for ordering
	data_list = [
				counter["Sunday"],
				counter["Monday"],
				counter["Tuesday"],
				counter["Wednesday"],
				counter["Thursday"],
				counter["Friday"],
				counter["Saturday"]]
	day_tuple = tuple(["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"])

	# Assign the data to a plot
	plt.plot(self.data_list)
	plt.xticks(range(len(day_tuple)), day_tuple)
	plt.savefig("Days.png")
	plt.clf()
	return self.headers

def visualize_type():
	#Parse data

	#Make a counter from each category
	counter = Counter(item["Category"] for item in data_file)
	#Set labels
	labels = tuple(counter.keys())
	#Locations on x-axis
	xlocations = na.array(range(len(labels))) + 0.5
	
	width = .5
	
	plt.bar(xlocations, counter.values(), width)
	plt.xticks(xlocations + width / 2, labels, rotation = 90)
	plt.subplots_adjust(bottom = .5)
	plt.rcParams['figure.figsize'] = 12, 8
	plt.savefig("Type.png")
	plt.clf()

	return

