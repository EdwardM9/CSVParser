"""
CSV Parsing Utility

Takes in parsed data from a CSV file and renders it onto a chart.
Prefers rendering simple data, such as sets of plot points. More
complex charting can be done, but it requires custom scripting for
each specialized chart.

Parses a CSV file.

Copyright(c) 2014 Edward Moreno
Distributed under the Creative Commons Attribution 3.0 Unported license.
"""

import csv

def parse(raw_file, delimiter):
	""" Parses a raw CSV file to a JSON-line style object. """

	opened_file = open(raw_file)
	csv_data = csv.reader(opened_file, delimiter = delimiter)

	parsed_data = []
	fields = csv_data.next()

	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))
	opened_file.close()

	# Build data structure
	return parsed_data, fields

