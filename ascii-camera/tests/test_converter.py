import unittest
from src.ascii.converter import AsciiConverter

class TestAsciiConverter(unittest.TestCase):

    def setUp(self):
        self.converter = AsciiConverter()

    def test_convert_frame_to_ascii(self):
        # Assuming the converter has a method to convert a frame to ASCII
        frame = [[0, 0, 0], [255, 255, 255]]  # Example frame
        ascii_art = self.converter.convert_frame_to_ascii(frame)
        self.assertIsInstance(ascii_art, str)

    def test_empty_frame(self):
        frame = []  # Empty frame
        ascii_art = self.converter.convert_frame_to_ascii(frame)
        self.assertEqual(ascii_art, "")

if __name__ == '__main__':
    unittest.main()