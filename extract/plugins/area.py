"""
Plugin to extract data from area given by coordinates
"""

import pdftotext
import re
import logging

logger = logging.getLogger(__name__)

DEFAULT_OPTIONS = {'This is default setting'}

print("Within plugin file")

def extract(self, content, output):
    print('Within extract function')
    """Try to extract tables from an invoice"""
    for area in self['area']:
        print('Within loop')
        print(area)
        # First apply default options.
        plugin_settings = DEFAULT_OPTIONS.copy()
        plugin_settings.update(area)
        area = plugin_settings
        print("Area:", area)
        # Validate settings
        assert 'X-Coordinate' in area, 'x-coordinate missing'
        assert 'Y-Coordinate' in area, 'y-coordinate missing'
        # assert 'Width' in area, 'Area width regex missing'
	    # assert 'Height' in area, 'Area Height missing'
		
        x = re.search(area['X-Coordinate'], content)
        y = re.search(area['Y-Coordinate'], content)

        if not x or not y:
            logger.warning('no area body found - x %s, y %s', x, y)
            print("Please work")
