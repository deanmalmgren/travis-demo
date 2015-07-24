import unittest

import mike

class MikeTest(unittest.TestCase):

    def test_choices(self):
        self.assertIn('at life', mike.things_that_mike_sucks_at)
