from setuptools import setup, find_packages
import os
import sys

__version__ = '0.0.0'
__requirements__ = [
    "django==1.8",
]

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

setup(
    name='django-audio-recorder',
    version=__version__,
    packages=find_packages('audio_recorder'),
    install_requires=__requirements__,
)
