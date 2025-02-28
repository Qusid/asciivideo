import cv2

class AsciiConverter:
    def __init__(self, width=200):
        self.width = width
        self.ascii_chars = "@%#*+=-:. "

    def convert_frame_to_ascii(self, frame):
        """
        Converts a given frame to its ASCII representation.

        :param frame: The frame to convert
        :return: The ASCII representation of the frame
        """
        if frame is None:
            raise ValueError("Frame cannot be None")

        height, width, _ = frame.shape
        aspect_ratio = height / width
        new_height = int(aspect_ratio * self.width * 10)
        resized_frame = cv2.resize(frame, (self.width, new_height))
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        ascii_image = ""

        for pixel_value in gray_frame.flatten():
            if pixel_value is None:
                raise ValueError("Pixel value cannot be None")
            ascii_image += self.ascii_chars[pixel_value // 32]

        return ascii_image
