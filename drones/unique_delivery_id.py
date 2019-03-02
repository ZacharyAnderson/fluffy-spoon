import unittest

# Each Drone has unique ID - int
# every time a drone takes off for delivery we add it to the list
# when it returns we add it again to the list
# So each id should be on the list twice, find the missing ID


def find_unique_delivery_id(delivery_ids):

    # Find the one unique ID in the list
    # N runtime but N space
    # unique_id_dict = {}
    # for id in delivery_ids:
    #     if id in unique_id_dict:
    #         unique_id_dict[id] = False
    #     else:
    #         unique_id_dict[id] = True
    # for id in delivery_ids:
    #     if unique_id_dict[id] == 1:
    #         return id

    unique_id = 0
    
    for delivery_id in delivery_ids:
        unique_id ^= delivery_id
        print(unique_id)
    print("\n")
    return unique_id



# Tests

class Test(unittest.TestCase):

    def test_one_drone(self):
        actual = find_unique_delivery_id([1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_comes_first(self):
        actual = find_unique_delivery_id([1, 2, 2])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_comes_last(self):
        actual = find_unique_delivery_id([3, 3, 2, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_in_middle(self):
        actual = find_unique_delivery_id([3, 2, 1, 2, 3])
        expected = 1
        self.assertEqual(actual, expected)

    def test_many_drones(self):
        actual = find_unique_delivery_id([2, 5, 4, 8, 6, 3, 1, 4, 2, 3, 6, 5, 1])
        expected = 8
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)