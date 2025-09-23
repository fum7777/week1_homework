def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

    return weather_information

    # Q1. 全国の平均気温を計算してください(9.5となればOK)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)


def get_average_temperature(result):
    temp_list = [t["temperature"] for t in result]
    return sum(temp_list) / len(temp_list)


def get_average_temperature_by_pref(result, prefecture):
    temp_list = [t["temperature"] for t in result if t["prefecture"] == prefecture]
    return sum(temp_list) / len(temp_list)


def get_station_by_pref(result, prefecture):
    stations = [s["station"] for s in result if s["prefecture"] == prefecture]
    return ",".join(stations)


if __name__ == "__main__":
    result = main()

    # print(f"{get_average_temperature(result)} ℃")
    # print(repr(get_station_by_pref(result, "大阪府")))
    # print(f"{get_average_temperature_by_pref(result, '福岡県')} ℃")

print(
    f"全国 平均気温: {get_average_temperature(result)} ℃\n"
    f"大阪府の駅: {repr(get_station_by_pref(result, "大阪府"))}\n"
    f"福岡 平均気温{get_average_temperature_by_pref(result, '福岡県')} ℃"
)
