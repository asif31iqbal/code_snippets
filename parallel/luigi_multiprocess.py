import luigi
import json_mapper

THRESHOLD = 1.99


class TestTask(luigi.Task):
    file_number = luigi.Parameter()

    def input(self):
        return luigi.LocalTarget('data/dat_{}.json'.format(self.file_number))

    def output(self):
        return luigi.LocalTarget('out_data2/out_{}.json'
                                 .format(self.file_number))

    def run(self):
        with self.output().open('w') as out_file:
            with self.input().open('r') as in_file:
                for line in in_file:
                    for out in json_mapper.map_line(line, THRESHOLD):
                        out_file.write(out)



class LotsOTasks(luigi.WrapperTask):

    def requires(self):
        for k in range(4):
            yield TestTask(file_number=k)


if __name__ == '__main__':
    luigi.run()
