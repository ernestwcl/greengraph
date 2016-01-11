from setuptools import setup, find_packages

setup(

	name = "Greengraph",
	version = "0.1",
	description = "Python assignment",
	author = "Ernest Lo",
	packages = find_packages(exclude=['*test']),
	scripts = ['scripts/run.py'],
	install_requires = ['geopy','numpy','matplotlib','requests','argparse']
	)
	