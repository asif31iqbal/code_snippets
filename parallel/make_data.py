import numpy as np
import json
import os


"""
makes files named dat_{num}.json with lines like:

{"index":[random number], "total":[random number]}
{"index":[random number], "total":[random number]}
{"index":[random number], "total":[random number]}
...

"""


num_files = 4
lines_per_file = 1000000
directory = 'data'

os.system('mkdir {}'.format(directory))


for file_name in range(num_files):
    out_file = '{}/dat_{}.json'.format(directory,
                                       file_name)

    os.system('touch {}'.format(out_file))
    with open(out_file, 'w') as f:
        for l in np.random.rand(lines_per_file, 2):
            f.write(json.dumps({'index': l[0], 'total': l[1]}) + '\n')
