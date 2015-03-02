# testDoctests.py

from unittest import TestSuite 
from doctest import DocFileSuite
from doctest import ELLIPSIS
from doctest import NORMALIZE_WHITESPACE


__author__ = "Sean Chen"
__email__ = "sean.chen@leocorn.com"

optionflags = (ELLIPSIS | NORMALIZE_WHITESPACE)

# set up the testing enviroment.
def setUp(test):
    # nothing for now.
    return

def test_suite():

    suite = TestSuite()

    # add the main README.rst
    suite.addTest(
        DocFileSuite(
            'README.rst',
            package='leocornus.py.sandbox',
            setUp=setUp,
            optionflags=optionflags,
            ),
        )

    suite.addTest(
        DocFileSuite(
            'tests/basicPython.rst',
            package='leocornus.py.sandbox',
            ),
        )

    # hold this for now, we might not depend on fabric.
    #suite.addTest(
    #    DocFileSuite(
    #        'tests/basicLocalFabric.rst',
    #        package='leocornus.recipe.distribute',
    #        ),
    #    )

    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
