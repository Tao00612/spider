import win32gui
import win32api
import win32con
# hwnd_title = {}
#
#
# def get_all_hwnd(hwnd, mouse):
#     if (win32gui.IsWindow(hwnd)
#             and win32gui.IsWindowEnabled(hwnd)
#             and win32gui.IsWindowVisible(hwnd)):
#         hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
#
#
# win32gui.EnumWindows(get_all_hwnd, 0)
# for h, t in hwnd_title.items():
#     if t:
#         print(h, t)

# 句柄
wdname = u'查找'

hwnd = win32gui.FindWindow(None, wdname) # 父句柄
# 句柄id
print(hwnd)
# 放在前面
# win32gui.SetForegroundWindow(hwnd)
# 获取标题
title = win32gui.GetWindowText(hwnd)
print(title)

# 获取类名
clsname = win32gui.GetClassName(hwnd)
print(clsname)

# 分别为左、上、右、下的窗口位置
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
print(left, top, right, bottom)

win32api.SetCursorPos([left+150, top+100])
# 根据横纵坐标定位光标
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
# 给光标定位的位置进行单击操作（若想进行双击操作，可以延时几毫秒再点击一次）
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
# 给光标定位的位置进行右击操作



