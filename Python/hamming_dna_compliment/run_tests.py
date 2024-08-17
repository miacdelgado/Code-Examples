import unittest

import tests_strings

suite = unittest.TestLoader().loadTestsFromModule(tests_strings)
unittest.TextTestRunner(verbosity=2).run(suite)