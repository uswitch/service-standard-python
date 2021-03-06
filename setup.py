from setuptools import setup

setup(
    name='service-standard-python',
    version='0.2',
    description='RVU Service Standard library for Python',
    url='git@github.com:uswitch/service-standard-python.git',
    author='Site Reliability Engineering',
    author_email='sre@rvu.co.uk',
    install_requires=['flask', 'prometheus_client', 'werkzeug'],
    packages=['service_standard_python'],
    zip_safe=False
)
