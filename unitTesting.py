import unittest

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.stack:
            raise indexError("Cannot pop from empty stack")
        return self.stack.pop()
    def peak(self):
        return self.stack[-1]
    def in_empty(self):
        if len(self.stack) > 0:
            return False
        return True 


class StackTests(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        del self.stack
    
    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_push(self):
        self.stack.push(100)
        self.assertFalse(self.stack.is_empty())

    def test_peak(self):
        self.stack.push('test')
        self.assertEqual(self.stack.peak(), "test")

    def test_pop(self):
        self.stack.push(10.1)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_pop_value(self):
        self.stack.push("test_value")
        value = self.stack.pop()
        self.assertEqual(value, 'test_value')
