import luigi
import json_mapper
from luigi.contrib.spark import PySparkTask, SparkSubmitTask


class TestTaskPS(PySparkTask):

    def input(self):
        return luigi.LocalTarget('data/dat_0.json')

    def output(self):
        return luigi.LocalTarget('out_data3/')


    def main(self, sc, *args):
        lines = sc.textFile(self.input().path)
        lines.flatMap(json_mapper.map_line).saveAsTextFile(self.output().path)



if __name__ == '__main__':
    luigi.run()
