from setuptools import setup

setup(
    name='service-standard-python',
    version='0.0.1',
    description='RVU Service Standard library for Python',
    url='git@github.com:uswitch/service-standard-python.git',
    author='Site Reliability Engineering',
    author_email='sre@rvu.co.uk',
    install_requires=['flask', 'prometheus_client'],
    packages=['service-standard-python'],
    zip_safe=False
)