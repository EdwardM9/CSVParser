"""
Data Visualization

Copyright(c) 2014 E. Moreno
Distributed under the Creative Commons Attribution 3.0 Unported license.
"""

import csv

def parse(raw_file, delimiter):
	""" Parses a raw CSV file to a JSON-line object. """

	opened_file = open(raw_file)
	csv_data = csv.reader(opened_file, delimiter = delimiter)

	parsed_data = []
	fields = csv_data.next()

	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))
	opened_file.close()

	# Build data structure
	return parsed_data, fields

