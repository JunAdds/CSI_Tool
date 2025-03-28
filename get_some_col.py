import pandas as pd
#擷取某時間段資料

# 檔案名稱
filename = '1009Data/ap2/filtered_20241009AP2WALK_2P.csv'

# 讀取CSV文件，跳過格式不正確的行
df = pd.read_csv(filename, on_bad_lines='skip')

# 處理時間列，將時間轉換為datetime對象
df['time'] = pd.to_datetime(df['time'], format='%m/%d %H:%M:%S.%f', errors='coerce')

# 檢查是否有無效的時間值
if df['time'].isna().any():
    print("Warning: Some time values could not be converted and are set to NaT")

# 定義時間區間
start_time = '10/09 22:49:17.000'
end_time = '10/09 22:49:20.000'

# 將時間區間轉換為datetime對象
start_time = pd.to_datetime(start_time, format='%m/%d %H:%M:%S.%f')
end_time = pd.to_datetime(end_time, format='%m/%d %H:%M:%S.%f')

# 篩選出特定時間區間的資料
filtered_df = df[(df['time'] >= start_time) & (df['time'] <= end_time)]

# 將時間列格式化為所需的格式
filtered_df['time'] = filtered_df['time'].dt.strftime('%m/%d %H:%M:%S.%f')

# 將篩選後的資料寫入新的CSV文件
filtered_df.to_csv('1009Data/test1234.csv', index=False)