from setuptools import setup, find_packages


setup(
    name='picture-to-burn',
    packages=find_packages(),
    install_requires=[
        'docopt',
        'lxml',
        'requests',
    ],
    scripts=['bin/create_gif'],
    version='0.0.1',
)
