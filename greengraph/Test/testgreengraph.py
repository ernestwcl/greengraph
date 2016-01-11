import os
import numpy as np
import unittest
import yaml

from greengraph import *
from nose.tools import *
from mock import Mock, patch

def test_geolocate():
    with open(os.path.join(os.path.dirname(__file__),'fixtures','mapcoord.yaml')) as fixtures_file:
	    fixtures = yaml.load(fixtures_file)
	    for fixt in fixtures:
		    location = fixt.pop('location')    
		    lat = fixt.pop('lat')
		    long = fixt.pop('long')
		    answer = (lat,long)
	    
		    Trial = Greengraph(0.0,0.0)
		    assert_equal(Trial.geolocate(location), answer)
			
			

def test_location_sequence():
    with open(os.path.join(os.path.dirname(__file__),'fixtures','locationsequence.yaml')) as fixtures_file:
	    fixtures = yaml.load(fixtures_file)
	    for fixt in fixtures:
		    orig = fixt.pop('orig') 
		    dest = fixt.pop('dest')
		    step = fixt.pop('steps')  
		    lat = fixt.pop('lat')
		    long = fixt.pop('long')		    
		    Trial = Greengraph(0.0,0.0)
		    answer = Trial.location_sequence(Trial.geolocate(orig),Trial.geolocate(dest),step)
		    assert(answer[fixt][1]==long and answer[fixt][o]==lat)	
