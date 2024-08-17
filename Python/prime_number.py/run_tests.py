import unittest

import prime_tests

suite = unittest.TestLoader().loadTestsFromModule(prime_tests)
unittest.TextTestRunner(verbosity=2).run(suite)