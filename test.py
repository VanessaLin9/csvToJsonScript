import csv
import json

csv_file_path = './QueryResult_0130-053617.csv'
batch_size = 3000
skip_rows = 0


def csv_to_json(csv_file_path, skip_rows):
    json_data = {
        "Players": [],
        "Provider": [1]  
    }

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for i, row in enumerate(reader, start=1):
            playerId = row["PlayerID"]
            startDate = "2023-12-01T00:00:00.000Z"
            endDate = "2023-12-31T00:00:00.000Z"
  
            if i <= skip_rows:
                continue
            # 構建JSON結構
            player_data = {
                "customerId": playerId,
                "periods": [
                    {
                        "startDate": startDate,
                        "endDate": endDate
                    }
                ]
            }

            # 將構建的結構添加到jPlayer
            json_data["Players"].append(player_data)
            if len(json_data["Players"]) >= batch_size:
                break

    return json_data


while True:
    result_json = csv_to_json(csv_file_path, skip_rows)
    if not result_json["Players"]:
        break

# 使用CSV文件進行轉換
    json_string = json.dumps(result_json, ensure_ascii=False, indent=4)
    output_file_path = f'Players_{skip_rows+2}_{skip_rows+2+len(result_json["Players"])}.json'

# 將轉換後的JSON數據寫入文件
    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_string)

    print(json_string)

    skip_rows += len(result_json["Players"])