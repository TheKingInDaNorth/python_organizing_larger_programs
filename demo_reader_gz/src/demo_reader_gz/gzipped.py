import gzip
from demo_reader3.util import writer

extension = '.gz'
opener = gzip.open
if __name__ == '__main__':
    writer.main(opener)