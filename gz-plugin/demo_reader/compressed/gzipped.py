import gzip
from ..util import writer

extension = '.gz'
opener = gzip.open
if __name__ == '__main__':
    writer.main(opener)