import unittest


def is_valid(code):

    # Determine if the input code is valid
    openers_to_closers = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    openers = set(openers_to_closers.keys())
    closers = set(openers_to_closers.values())
    
    openers_stack = []
    for ch in code:
        if ch in openers:
            openers_stack.append(ch)
        elif ch in closers:
            if not openers_stack:
                return False
            else:
                last_unclosed_opener = openers_stack.pop()
                if not openers_to_closers[last_unclosed_opener] == ch:
                    return False
                    
    return openers_stack == []


















# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)