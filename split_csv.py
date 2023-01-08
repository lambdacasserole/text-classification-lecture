# Script for breaking down a 2-column CSV file into separate files.
#
# Copyright (C) Saul Johnson 2022
# Author: Saul Johnson <saul.a.johnson@gmail.com>
# Usage: python3 split_csv.py <filename>
#
# Used for a 2022 guest lencture at NHL Stenden Leeuwarden.

import sys
import csv


# Open the file specified on the command line (you may have to fiddle with 'encoding' below).
with open(sys.argv[1], encoding='latin-1') as input_file:

    # Read CSV file and loop over rows.
    first = True
    counts = {}
    reader = csv.reader(input_file)
    for row in reader:

        # Skip first (title) row and any invalid rows.
        if first or len(row) < 2:
            first = False
            continue

        # Keep track of the current count for this class.
        if row[0] not in counts:
            counts[row[0]] = 0
        counts[row[0]] += 1

        # Break row out into text file.
        with open(f'./{row[0]}/{row[0]}_{counts[row[0]]}.txt', 'w') as text_file:
            print(row[1], file=text_file)
