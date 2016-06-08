import json
import sys

THRESHOLD = 1.99


def map_line(line, th=THRESHOLD):
    line_dict = json.loads(line)
    sum_val = line_dict['index'] + line_dict['total']
    if sum_val > th:
        line_dict['sum_val'] = sum_val
        yield json.dumps(line_dict)


if __name__ == '__main__':
    for line in sys.stdin:
        for out in map_line(line, THRESHOLD):
            print out

