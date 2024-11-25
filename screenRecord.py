import cv2
import numpy as np
import pyautogui
import datetime


screen_width, screen_height = pyautogui.size()

current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_filename = f'capture{current_time}.avi'
fps = 30.0 #framerate 

out = cv2.VideoWriter(output_filename, fourcc, fps, (screen_width, screen_height))

while True:
    #capture scree
    screenshot = pyautogui.screenshot()
    
    #convert screenshots to numpy array and change colour to BGR
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    out.write(frame)
    
    #v2.imshow('Recording....', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cv2.destroyAllWindows()

