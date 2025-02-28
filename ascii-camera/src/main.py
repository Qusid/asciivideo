import tkinter as tk
from camera.capture import CameraCapture
from ascii.converter import AsciiConverter

class AsciiVideoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ASCII Video")
        
        # Configure text widget for ASCII display
        self.text_widget = tk.Text(
            root,
            font=('Courier', 1),  # Monospace font
            bg='black',
            fg='white',
            height=1000,
            width=1000
        )
        self.text_widget.pack()

        # Initialize camera and converter
        self.camera = CameraCapture()
        self.ascii_converter = AsciiConverter()
        self.camera.initialize_camera()

        # Start the update loop
        self.update_frame()

    def update_frame(self):
        # Capture and convert frame
        frame = self.camera.capture_frame()
        ascii_art = self.ascii_converter.convert_frame_to_ascii(frame)
        
        # Update text widget
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, ascii_art)
        
        # Schedule next update
        self.root.after(16, self.update_frame)  # 16ms -> 60fps

def main():
    root = tk.Tk()
    root.geometry("1024x768")  # Set the window size to 1024x768
    app = AsciiVideoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()