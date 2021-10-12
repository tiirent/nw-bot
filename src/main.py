import cv2 as cv
import numpy as np
import os
import pyautogui
from time import time
from service.windowcapture import WindowCapture
from service.screengrab import ScreenGrab
from service.vision import Vision
from model.hsvfilter import HsvFilter
from model.hsvfilterconfig import HsvFilterConfig
from bot import Bot

bot = Bot()

screenGrab = ScreenGrab(2440//4, 1080, 1440//2, 0)
hookVision = Vision('./hook_processed.jpg')
reelVision = Vision('./reel_processed.jpg')
successVision = Vision('./success_processed.jpg')

# creates gui
# hookVision.init_control_gui()
loop_time = time()
while(True):
    # init
    screenshot = screenGrab.get_screenshot()
    hook_points = []
    reel_points = []
    success_points = []

    # process images
    if bot.getState() == 'idle':
        processed_hook_img = hookVision.apply_hsv_filter(screenshot, HsvFilterConfig.getFishIconFilter())
        hook_points = hookVision.find(processed_hook_img, 0.7, 1, False)
        screenshot = hookVision.draw_rectangles(screenshot, hook_points, True)
    else:
        processed_reel_img = reelVision.apply_hsv_filter(screenshot, HsvFilterConfig.getReelFilter())
        processed_success_img = successVision.apply_hsv_filter(screenshot, HsvFilterConfig.getSuccessFilter())
        
        reel_points = reelVision.find(processed_reel_img, 0.4, 1, False)
        success_points = successVision.find(processed_success_img, 0.7, 1, False)

        screenshot = reelVision.draw_rectangles(screenshot, reel_points, True)
        screenshot = successVision.draw_rectangles(screenshot, success_points, True)


    # calculate distance / do action
    bot.fish(hook_points, reel_points, success_points)

    # display the processed image
    # cv.imshow('Processed', wraith.apply_hsv_filter(screenshot))
    cv.imshow('Matches', screenshot)

    # debug the loop rate
    # print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
