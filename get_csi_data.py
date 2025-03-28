import os
import serial
import csv
import datetime

#獲取CSI數據

# 指定目標資料夾
target_folder = 'test'  # 目標資料夾名稱

# 檢查文件並確定新文件名稱
def check_and_get_filename():
    prefix = 'testap1'
    # 確保目標資料夾存在，如果不存在則創建s
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    existing_files = [f for f in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, f)) and f.startswith(prefix) and f.endswith('.csv')]
    max_num = 0
    for file in existing_files:
        parts = file.replace('.csv', '').split('_')
        if len(parts) > 1 and parts[-1].isdigit():
            num = int(parts[-1])
            max_num = max(max_num, num)
    new_filename = prefix + str(max_num + 1) + '.csv'
    return os.path.join(target_folder, new_filename)  # 返回完整的文件路徑

# 接收器放在哪個地方
ser1 = serial.Serial('/dev/tty.wchusbserial130', 921600)  # 第一個AP的串口
#ser2 = serial.Serial('/dev/tty.wchusbserial130', 921600)  # 第二個AP的串口
csi_count = 0
num = 0

filename = check_and_get_filename()  # 獲取新文件名稱
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    headers = ["time", "ap", "type", "role", "mac", "rssi", "rate", "sig_mode", "mcs", "bandwidth", "smoothing", "not_sounding", "aggregation", "stbc", "fec_coding", "sgi", "noise_floor", "ampdu_cnt", "channel", "secondary_channel", "local_timestamp", "ant", "sig_len", "rx_state", "real_time_set", "real_timestamp", "len", "CSI_DATA"]
    writer.writerow(headers)

    while csi_count < 20000:
        for ser, ap_name in [(ser1, "AP2")]:
            line = ser.readline()
            try:
                line_str = line.decode('utf-8', errors='replace').replace('\r\n', '')  # 使用 'replace' 選項
            except UnicodeDecodeError:
                continue  # 如果仍然有解碼錯誤，則跳過此行

            data_list = line_str.split(',')

            if "CSI_DATA" in line_str:
                current_time = datetime.datetime.now().strftime("%m/%d %H:%M:%S.%f")[:-3]
                data_list.insert(0, ap_name)  # 将AP名称插入数据列表的开头
                data_list.insert(0, current_time)  # 将时间插入数据列表的开头
                writer.writerow(data_list)  # 写入数据
                csi_count += 1

            print(data_list)

print("done")