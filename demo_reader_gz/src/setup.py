import setuptools

setuptools.setup(
    name="demo_reader_3_gz_plugin",
    version="0.0.0",
    description="demo_reader plugin for reading gz files",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'demo_reader3.compression_plugins': [
            'gz = demo_reader_gz.bzipped'
        ]
    }
)