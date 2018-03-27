import sys
import time
import numpy as np

from prettytable import PrettyTable

ncols = 4
nrows = 4

col_labels = [" "*5] + ["col_{0}".format(i) for i in range(ncols)]
row_labels = ["row_{0}".format(i) for i in range(nrows)]

def print_table():

    data = np.random.random((ncols, nrows))

    table = PrettyTable(col_labels)
    table.float_format = ".10"

    for row_idx in range(nrows):
        table.add_row([row_labels[row_idx]] + data[:, row_idx].tolist())

    for field_name in table.field_names:
        table.align[field_name] = 'r'

    print(table, end='\r')

num_lines = nrows + 3

def reset_cursor():
    for i in range(num_lines):
        sys.stdout.write("\033[F")

print_table()

while True:
    time.sleep(3)

    reset_cursor()
    print_table()
