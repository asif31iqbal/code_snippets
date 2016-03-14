import luigi
import json_mapper
import luigi.contrib.hadoop
import luigi.contrib.hdfs

THRESHOLD = 1.99


class InData(luigi.Task):

    def output(self):
        return luigi.contrib.hdfs.HdfsTarget('data')


class TestTaskMR(luigi.contrib.hadoop.JobTask):

    def requires(self):
        return InData()

    def output(self):
        return luigi.contrib.hdfs.HdfsTarget('out_data6')

    def mapper(self, line):
        for out in json_mapper.map_line(line, THRESHOLD):
            yield out+'\n',


if __name__ == '__main__':
    luigi.run()
