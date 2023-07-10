import setuptools
import os


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as fp:
        s = fp.read()
    return s


def get_version(path):
    with open(path, "r") as fp:
        lines = fp.read()
    for line in lines.split("\n"):
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name='ipasymbols',
    version=get_version("ipasymbols/__init__.py"),
    description='Properties of IPA symbols for data analysis.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='http://github.com/ulf1/ipasymbols',
    author='Ulf Hamster',
    author_email='554c46@gmail.com',
    license='Apache License 2.0',
    packages=['ipasymbols'],
    install_requires=[
        'numpy>=1.21.4,<2'
    ],
    python_requires='>=3.6',
    zip_safe=True
)
