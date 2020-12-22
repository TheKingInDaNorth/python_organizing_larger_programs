import setuptools

setuptools.setup(
    name="demo_reader_3_bz2_plugin",
    version="0.0.0",
    description="demo_reader plugin for reading bz2 files",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'demo_reader3.compression_plugins': [
            'bz2 = demo_reader_bz2.bzipped'
        ]
    }
)