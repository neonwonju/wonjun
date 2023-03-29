'''
import pyautogui

# alt + tab 키 누르기
pyautogui.hotkey('alt', 'tab')
'''

import pyautogui

def alt_tab():
    # alt + tab 키 누르기
    pyautogui.hotkey('alt', 'tab')

# 사용자 입력 대기
input("alt + tab을 누르려면 엔터 키를 누르세요.")

# alt + tab 실행
alt_tab()
