import pyautogui
import time
import pyperclip

# Chờ 5 giây để bạn có thể chuyển sang trình duyệt và chọn ô văn bản
time.sleep(5)

# Paste văn bản đã được copy bằng cách nhấn tổ hợp phím "Ctrl" + "V"
pyautogui.hotkey('ctrl', 'v')

# Lưu văn bản đã paste vào biến tex

# Lấy dữ liệu từ clipboard
text = pyperclip.paste()

# In văn bản đã lấy ra
print(text)
# In văn bản ra màn hình console