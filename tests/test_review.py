#!/usr/bin/python3
"""Testerino"""

import unittest
import models.review import Review


class test_creview(unittest.TestCase):
    """tests review"""
    def test_review(self):
        rv = Review()
        self.assertEqual(review_1.place_id, "")
        self.assertEqual(review_1.user_id, "")
        self.assertEqual(review_1.text, "")

if __name__ == '__main__':
    unittest.main()
