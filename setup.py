from setuptools import setup, find_packages


setup(
    name='picture-to-burn',
    packages=find_packages(),
    install_requires=[
        'python-twitter',
        'docopt',
    ],
    scripts=['bin/create_gif'],
    data_files=[('data', ['twitter_creds.json'])],
    version='0.0.1',
)
