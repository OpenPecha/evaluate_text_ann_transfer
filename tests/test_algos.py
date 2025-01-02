from unittest import TestCase

from text_ann_transfer import (
    transfer_coordinate_difflib,
    transfer_coordinate_google,
    transfer_coordinate_levenshtein,
    transfer_coordinate_openpecha,
)


class TestTextAnnTransferAlgorithms(TestCase):
    def setUp(self):
        self.source_text = "Hello World!"
        self.target_text = "Hello, World!"
        self.source_coordinate = 6  # Position of 'w' in source_text

    def test_transfer_coordinate_openpecha(self):
        target_coordinate = transfer_coordinate_openpecha(
            self.source_text, self.target_text, self.source_coordinate
        )
        self.assertEqual(target_coordinate, 7)

    def test_transfer_coordinate_google(self):
        target_coordinate = transfer_coordinate_google(
            self.source_text, self.target_text, self.source_coordinate
        )
        self.assertEqual(target_coordinate, 7)

    def test_transfer_coordinate_difflib(self):
        target_coordinate = transfer_coordinate_difflib(
            self.source_text, self.target_text, self.source_coordinate
        )
        self.assertEqual(target_coordinate, 7)

    def test_transfer_coordinate_levenshtein(self):
        target_coordinate = transfer_coordinate_levenshtein(
            self.source_text, self.target_text, self.source_coordinate
        )
        self.assertEqual(target_coordinate, 7)

    def tearDown(self):
        del self.source_text
        del self.target_text
        del self.source_coordinate
