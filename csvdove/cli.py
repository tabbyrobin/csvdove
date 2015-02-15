import sys

# there is not much CLI, i can probably integrate it back into main.CSVDove
class CLI(object):
    def __init__(self, schema_file, list_of_src_files, o=sys.stdout):
        self.schema_file = schema_file
        self.source_files_list = list_of_src_files

        self.output_file = o
    
    def main(self):
        from data import DataWrapper
        from worker import Worker
        data = DataWrapper(self.schema_file, self.output_file,
                           self.source_files_list)
        w = Worker(data)
        w.main()


        