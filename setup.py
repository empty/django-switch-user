import os
from setuptools import setup, find_packages


def read(fname):
    try:
        with open(os.path.join(os.path.dirname(__file__), fname)) as fh:
            return fh.read()
    except IOError:
        return ''

requirements = read('REQUIREMENTS').splitlines()
tests_requirements = read('REQUIREMENTS-TESTS').splitlines()

setup(
    name="django-switch-user",
    version="0.1.0",
    description="Django Switch User allows you to assume the identity of another user.",
    long_description=read('README.rst'),
    url='http://michaeltrier.com',
    license='MIT',
    author='Michael Trier',
    author_email='mtrier@gmail.com',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
    ],
    install_requires=requirements,
    tests_require=tests_requirements,
)
