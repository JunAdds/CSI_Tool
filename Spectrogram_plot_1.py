import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import stft
#畫出時頻圖
filenames2 = ['1009Data/test1234.csv']

sampling_rate = 1408
# 處理每個文件
for filename in filenames2:
    # 讀取CSV文件，跳過格式不正確的行
    df = pd.read_csv(filename, header=None, on_bad_lines='skip')
    original_data = df.copy()  # 保存原始資料

    # 處理時間列，將時間轉換為datetime對象
    df[0] = pd.to_datetime(df[0], format='%m/%d %H:%M:%S.%f', errors='coerce')

    # 提取CSI數據列，去除方括號，轉換為數值
    csi_data2 = df.iloc[:, -1].str.replace('[', '').str.replace(']', '').str.split(expand=True)
    csi_data2 = csi_data2.apply(pd.to_numeric, errors='coerce')

    csi_data_int_lists2 = []
    for _, row in csi_data2.iterrows():
        # 將每個值轉換為整數，忽略NaN值
        int_list = [int(val) for val in row.dropna().values]
        csi_data_int_lists2.append(int_list)

    # 遍歷每一行的CSI數據，對每行繪製一張時頻圖
    for row_index, combined_csi_data2 in enumerate(csi_data_int_lists2):
        print(f"2np:{combined_csi_data2}")
        print(len(combined_csi_data2))
        if not combined_csi_data2:
            print(f"Row {row_index + 1} is empty, skipping...")
            continue

        f, t, Zxx = stft(combined_csi_data2, fs=sampling_rate, nperseg=20)

        if Zxx.ndim == 2:
            fig, ax1 = plt.subplots(figsize=(10, 6))

            pcm = ax1.pcolormesh(t, f, np.abs(Zxx), shading='gouraud')
            fig.colorbar(pcm, ax=ax1, label='Amplitude')
            ax1.set_title(f'STFT of Row {row_index + 1} in {filename}')
            ax1.set_ylabel('Frequency [Hz]')
            ax1.set_xlabel('Time [sec]')
            ax1.set_xlim(0, max(t))

            plt.show()
        else:
            print(f"STFT result for Row {row_index + 1} is not 2D, skipping...")

