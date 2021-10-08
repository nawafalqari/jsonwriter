from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='jsonwriter',
    version='0.1.4',
    description='Easy JSON Writer',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Nawaf Alqari',
    author_email='contact@nawaf.cf',
    packages=find_packages(where='jsonwriter'),
    python_requires='>=3.6',
    license='MIT',
    url = 'https://github.com/nawafalqari/jsonwriter',
    project_urls = {
        'Github': 'https://github.com/nawafalqari/jsonwriter',
        'Issues': 'https://github.com/nawafalqari/jsonwriter/issues',
    },
    keywords=['jsondb', 'json database', 'jsondatabase', 'json editor', 'json', 'json writer'],
    classifiers=[
    'Programming Language :: Python :: 3.6',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
  ],
)

# python setup.py sdist
# twine upload dist/jsonwriter-[version].tar.gz
