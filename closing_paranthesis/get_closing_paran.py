import unittest


def get_closing_paren(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    open_parans = 0
    
    for pos in xrange(opening_paren_index + 1, len(sentence)):
        char = sentence[pos]
        
        if char == '(':
            open_parans += 1
        elif char == ')':
            if open_parans == 0:
                return pos
            else:
                open_parans -= 1

    raise Exception("No closing Paranthesis mate!")


















# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)