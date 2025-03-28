import cv2
import datetime
import os
#純錄製影片

# 检查文件名是否存在的函数
def find_available_filename():
    base_name = "1009video_"
    extension = ".mp4"
    counter = 1
    while True:
        file_name = f"{base_name}{counter}{extension}"
        if not os.path.isfile(file_name):
            return file_name
        counter += 1

# 开启内建摄像头
cap = cv2.VideoCapture(1)

# 检查摄像头是否成功开启
if not cap.isOpened():
    print("无法开启摄像头")
    exit()

# 获取摄像头的解析度
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# 定义编码器并创建VideoWriter对象（MP4格式）
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v'为MP4格式的编码器

# 使用find_available_filename函数来获取一个不重复的文件名
output_filename = find_available_filename()
output = cv2.VideoWriter(output_filename, fourcc, 20.0, (frame_width, frame_height))

while True:
    # 从摄像头捕获一帧
    ret, frame = cap.read()

    # 如果正确读取了一帧，ret是True
    if not ret:
        print("无法读取摄像头画面")
        break

    # 应用镜像效果
    frame = cv2.flip(frame, 1)

    # 获取当前的日期和时间
    datetime_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3]

    # 在画面右下角添加日期和时间
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, datetime_str, (10, frame_height - 10), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    # 写入帧到文件
    output.write(frame)

    # 显示结果帧
    cv2.imshow('Camera', frame)

    # 按下 'q' 键停止录像
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头和VideoWriter对象
cap.release()
output.release()
# 关闭所有OpenCV窗口
cv2.destroyAllWindows()
