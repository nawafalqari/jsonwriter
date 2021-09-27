from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='jsonwriter',
    version='0.0.5',
    description='Easy JSON Writer',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Nawaf Alqari',
    author_email='nawafalqari13@gmail.com',
    packages=['jsonwriter'],
    license='MIT',
    url = 'https://github.com/nawafalqari/jsonwriter',
    keywords=['jsondb', 'json database', 'jsondatabase', 'json editor', 'json', 'json writer'],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)