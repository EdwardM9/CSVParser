"""
Data Visualization

Copyright(c) 2014 E. Moreno
Distributed under the Creative Commons Attribution 3.0 Unported license.
"""

import csv

def parse(raw_file, delimiter):
	""" Parses a raw CSV file to a JSON-line object. """

	# Open the CSV File
	opened_file = open(raw_file)

	# Read the CSV File
	csv_data = csv.reader(opened_file, delimiter = delimiter)

	parsed_data = []
	#skip headers line
	fields = csv_data.next()

	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))
	# Close CSV File
	opened_file.close()

	# Build data structure
	return parsed_data, fields

def main():
    # Call our parse function and give it the needed parameters
    new_data = parse(MY_FILE, ",")

    # Let's see what the data looks like!
    print new_data


if __name__ == "__main__":
    main()
