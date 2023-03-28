import time
from PIL import ImageGrab

time.sleep(5) # 초 대기

for i in range(1, 11): # 초 간격으로 이미지10개 저장
    img = ImageGrab.grab()
    img.save("image{}.png".format(i))
    time.sleep(0.1)
