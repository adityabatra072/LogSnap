from datetime import datetime
import os
import pygame
import pygame.camera
import time

def capture_image(camera_device, image_path, resolution=(1280, 720)):
    pygame.camera.init()
    cam = pygame.camera.Camera(camera_device, resolution)
    cam.start()
    time.sleep(1)
    img = cam.get_image()
    pygame.image.save(img, image_path)
    cam.stop()
    pygame.camera.quit()

def send_telegram_message(image_path, caption):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.system(f'telegram-send --image {image_path} --caption "{caption} on {now}"')

def main():
    image_path = "C:\\Users\\ADITYA\\Desktop\\Image.jpg"
    camera_device = 0 #camera index check with list_cameras()
    
    try:
        capture_image(camera_device, image_path)
        send_telegram_message(image_path, "New Login")
    finally:
        if os.path.exists(image_path):
            os.remove(image_path)

if __name__ == "__main__":
    main()
