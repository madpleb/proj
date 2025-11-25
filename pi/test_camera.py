from picamera2 import Picamera2, Preview
import time

camera = Picamera2()

camera_config = camera.create_preview_configuration()
camera.configure(camera_config)

camera.start_preview(Preview.QTGL)
camera.start()

time.sleep(2)

camera.capture_file("test_photo.jpg")