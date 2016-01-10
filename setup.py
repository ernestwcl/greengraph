from setuptools import setup, find_packages

setup(

	name = "Greengraph",
	version = "0.1",
	packages = find_packages(exclude=['*test']),
	install_requires = ['geopy','numpy','matplotlib','requests','argparse']
	)
	