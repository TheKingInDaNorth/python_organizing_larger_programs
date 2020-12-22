import bz2

from demo_reader3.util import writer

extension = '.bz2'
opener = bz2.open

if __name__ == '__main__':
    writer.main(bz2.open)