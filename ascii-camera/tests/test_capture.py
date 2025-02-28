import unittest
from src.camera.capture import CameraCapture

class TestCameraCapture(unittest.TestCase):

    def setUp(self):
        self.camera = CameraCapture()

    def test_initialize_camera(self):
        self.assertTrue(self.camera.initialize_camera())

    def test_capture_frame(self):
        frame = self.camera.capture_frame()
        self.assertIsNotNone(frame)

    def test_release_camera(self):
        self.camera.release_camera()
        self.assertIsNone(self.camera.camera)

if __name__ == '__main__':
    unittest.main()