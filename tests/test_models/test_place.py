#!/usr/bin/python3
"""Testerino"""

import unittest
from models.place import Place


class test_cplace(unittest.TestCase):
    """tests place"""

    def test_place(self):
        pl = Place()
        self.assertEqual(place_1.name, '')
        self.assertEqual(place_1.city_id, '')
        self.assertEqual(place_1.user_id, '')
        self.assertEqual(place_1.description, '')
        self.assertEqual(place_1.number_rooms, 0)
        self.assertEqual(place_1.number_bathrooms, 0)
        self.assertEqual(place_1.max_guest, 0)
        self.assertEqual(place_1.price_by_night, 0)
        self.assertEqual(place_1.latitude, 0.0)
        self.assertEqual(place_1.longitude, 0.0)
        self.assertEqual(place_1.amenity_ids, [])

if __name__ == '__main__':
    unittest.main()
