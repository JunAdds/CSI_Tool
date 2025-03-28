import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

#將檔案畫出來

# 檔案名稱列表
filenames = ['test/testap11.csv']

# 為每個檔案繪製一個圖表
for i, filename in enumerate(filenames, 1):
    # 讀取CSV文件，跳過格式不正確的行
    df = pd.read_csv(filename, header=None, on_bad_lines='skip')

    # 處理時間列，將時間轉換為datetime對象
    df[0] = pd.to_datetime(df[0], format='%m/%d %H:%M:%S.%f', errors='coerce')

    # 檢查是否有無效的時間值
    if df[0].isna().any():
        print("Warning: Some time values could not be converted and are set to NaT")

    # 提取CSI數據列，去除方括號，轉換為數值
    csi_data = df.iloc[:, -1].str.replace('[', '').str.replace(']', '').str.split(expand=True)
    csi_data = csi_data.apply(pd.to_numeric, errors='coerce')



    # 繪製折線圖
    plt.figure(figsize=(20, 10))
    for column in csi_data.columns:
        plt.plot(df[0], csi_data[column])

    # 設置X軸的時間格式僅為小時:分鐘:秒
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    # 使用SecondLocator指定每10秒顯示一個刻度
    plt.gca().xaxis.set_major_locator(mdates.SecondLocator(interval=10))
    # 使用MaxNLocator限制Y軸的最大刻度數量
    plt.gca().yaxis.set_major_locator(plt.MaxNLocator(nbins=10))

    plt.xlabel('Time')
    plt.ylabel('CSI Value')
    plt.title(f'CSI Data {filenames}')
    plt.xticks(rotation=45)  # 旋轉時間標籤以改善顯示
    plt.show()

# data = csi_data.iloc[2].to_list() #1-77
# # 對數據進行傅立葉轉換
# fft_result = np.fft.fft(data)

# # 計算頻率軸
# freqs = np.fft.fftfreq(len(data))

# # 可視化結果
# plt.figure(figsize=(10, 6))

# # 實部
# plt.subplot(2, 1, 1)
# plt.plot(freqs, np.abs(fft_result))
# plt.title('Magnitude Spectrum')
# plt.xlabel('Frequency')
# plt.ylabel('Magnitude')

# # 虛部
# plt.subplot(2, 1, 2)
# plt.plot(freqs, np.angle(fft_result))
# plt.title('Phase Spectrum')
# plt.xlabel('Frequency')
# plt.ylabel('Phase (radians)')

# plt.tight_layout()
# plt.show()


# data = csi_data[63][1::].to_list() #0-127 正
# # 對數據進行傅立葉轉換
# fft_result = np.fft.fft(data)
# N = len(fft_result)

# # 計算頻率軸
# freqs = np.fft.fftfreq(len(data))

# freqs = freqs[:N//2] #->只取正



# # 可視化結果
# plt.figure(figsize=(10, 6))

# # 實部
# plt.subplot(2, 1, 1)
# plt.plot(freqs, np.abs(fft_result[:N//2])) #->只取正
# #plt.plot(freqs, np.abs(fft_result))

# plt.title('Magnitude Spectrum')
# plt.xlabel('Frequency')
# plt.ylabel('Magnitude')

# # 虛部
# plt.subplot(2, 1, 2)
# plt.plot(freqs, np.angle(fft_result[:N//2])) #->只取正
# #plt.plot(freqs, np.angle(fft_result))

# plt.title('Phase Spectrum')
# plt.xlabel('Frequency')
# plt.ylabel('Phase (radians)')

# plt.tight_layout()
# plt.show()