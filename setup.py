from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='twitter-bot-example',
    version='0.0.1',
    description='An example Python Twitter bot',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/shc261392/twitter-bot-example',
    author='S. H. Chien',
    author_email='shc261392@gmail.com',
    keywords='twitter bot',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'python-dotenv',
        'python-twitter',
        'schedule'
    ],
    extras_require={
        'test': ['pytest', 'coverage'],
    },
    entry_points={  # Optional
        'console_scripts': [
            'simple_tweet=scripts.simple_tweet:main',
            'random_tweet=scripts.random_tweet:main',
            'scheduled_random_tweet=scripts.scheduled_random_tweet:main',
        ],
    },
)
