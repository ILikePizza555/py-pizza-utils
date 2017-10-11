from pizza_utils import decs
import unittest


class TestEnforceState(unittest.TestCase):
    class StateObject:
        def __init__(self):
            self.state = 4

        @decs.enforce_state("state", 2)
        def s(self):
            return self.state + 1

    def setUp(self):
        self.o = TestEnforceState.StateObject()

    def test(self):
        with self.assertRaises(ValueError):
            self.o.s()
