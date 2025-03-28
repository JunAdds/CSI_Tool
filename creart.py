import json

#Create 標記json資料


def format_time_point(time_point):
    """將不含冒號和點的時間點格式化為 hh:mm:ss.sss"""
    return f"{time_point[:2]}:{time_point[2:4]}:{time_point[4:6]}.{time_point[6:]}"

def create_data_structure():
    """創建數據結構並讓用戶輸入時間點"""
    data_structure = {}
    for i in range(1, 2):
        key = f"data{i}"
        data_structure[key] = {"1p": [], "2p": [], "3p": []}
        print(f"請輸入 {key} 的時間點（格式: hhmmsssss）：")
        
        # # 輸入1p時間點
        # for j in range(20):
        #     time_point = input(f"輸入 {key} 的第 {j+1} 個 1p 時間點: ")
        #     formatted_time_point = format_time_point(time_point)
        #     data_structure[key]["1p"].append(formatted_time_point)

        # # 輸入2p時間點
        # for j in range(20):
        #     time_point = input(f"輸入 {key} 的第 {j+1} 個 2p 時間點: ")
        #     formatted_time_point = format_time_point(time_point)
        #     data_structure[key]["2p"].append(formatted_time_point)

        # 輸入3p時間點
        for j in range(6):
            time_point = input(f"輸入 {key} 的第 {j+1} 個 3p 時間點: ")
            formatted_time_point = format_time_point(time_point)
            data_structure[key]["1p"].append(formatted_time_point)
#2039175
        # # 輸入fall時間點
        # for j in range(2):
        #     time_point = input(f"輸入 {key} 的第 {j+1} 個 3p 時間點: ")
        #     formatted_time_point = format_time_point(time_point)
        #     data_structure[key]["fall"].append(formatted_time_point)

    return data_structure

# 創建數據結構
data_structure = create_data_structure()

# 將數據結構轉換為JSON格式並保存到文件
with open('1009_complete_label_3p.json', 'w') as json_file:
    json.dump(data_structure, json_file, indent=4)

print("JSON文件已成功創建")
#3 - 8
#2 - 6
#1 - 6