"""
Patent Reference Splitter
Coded by Daniel Ho Kwan Leung
Email: danielleungdaniel@gmail.com
GitHub: DHKLeung
Coded in 12,Jan,2018
For Professor Lu L.H. in Department of Business Management in National Taipei University of Technology
Academic use only
Usage:
In terminal/cmd: $python patent_reference_splitter.py <original csv address> <the column to be processed, column counted from 0> <output csv address> "<the splitting characters>"
Example 1: $python patent_reference_splitter data.csv 31 data_out.csv ";"
Example 2: $python patent_reference_splitter patent.csv 6 patent_out.csv " \n"
"""
import pandas as pd
import numpy as np
import sys
import codecs
print('****************************\n'\
    + 'Patent Reference Splitter\n'\
    + 'Coded by Daniel Ho Kwan Leung\n'\
    + 'Email: danielleungdaniel@gmail.com\n'\
    + 'GitHub: DHKLeung\n'\
    + 'Coded in 12,Jan,2018\n'\
    + 'For Professor Lu L.H. in Department of Business Management in National Taipei University of Technology\n'\
    + 'Academic use only\n'\
    + '****************************\n'\
)
data_address = sys.argv[1]
process_col = int(sys.argv[2])
out_address = sys.argv[3]
split_char = codecs.decode(sys.argv[4], 'unicode_escape')
num_total_output = 0
full_data = pd.read_csv(data_address).as_matrix()
for i in range(full_data.shape[0]):
    single_line = full_data[i, :].reshape(1, -1)
    prefix = single_line[0, 0:process_col]
    need_process = single_line[0, process_col]
    suffix = single_line[0, process_col + 1:]
    if type(need_process) != type(''):
        temp_list = [need_process]
    else:
        temp_list = need_process.split(split_char)
    num_total_output += len(temp_list)
    for j in temp_list:
        temp_reference = np.array(j)
        out_single_line = np.append(np.append(prefix, temp_reference), suffix)
        df = pd.DataFrame(out_single_line.reshape(1, -1))
        df.to_csv(out_address, mode='a', header=False, index=False)
    print(str(prefix[0,]) + ' has been processed, Percentage: ' + str(float('{0:.2f}'.format(((i + 1) / float(full_data.shape[0])) * 100.))) + '%')
print('Total Rows: ' + str(num_total_output))