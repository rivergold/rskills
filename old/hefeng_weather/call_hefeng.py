import os
import requests

def parse_weather_data(data: dict) -> list[str]:
    result = []
    idx_to_text = {
        0: "今天",
        1: "明天",
        2: "后天",
    }
    for idx, day in enumerate(data.get("daily", [])):
        date = day.get("fxDate", "未知")
        temp_max = day.get("tempMax", "未知")
        temp_min = day.get("tempMin", "未知")
        text_day = day.get("textDay", "未知")
        text_night = day.get("textNight", "未知")
        # precip = day.get("precip", "未知")
        result.append(
            f"📅 {idx_to_text.get(idx, '未知')}({date}) | "
            f"🔥 最高温 {temp_max}℃ | ❄️ 最低温 {temp_min}℃ | "
            f"☀️ 白天 {text_day} | 🌙 夜间 {text_night}"
        )
    return result

def get_weather_3d() -> dict:
	url = "https://nv6r6yrpr5.re.qweatherapi.com/v7/weather/3d"
	headers = {
		"X-QW-Api-Key": os.environ["QWEATHER_API_KEY"],
	}
	params = {
		"location": "101270101",
	}

	response = requests.get(url, headers=headers, params=params, timeout=10)
	response.raise_for_status()
	return response.json()


if __name__ == "__main__":
    data = get_weather_3d()
    parsed = parse_weather_data(data)
    for line in parsed:
        print(line)
