from main import check_bad_weather

def test_weather_conditions(): # top tests
    tests = {
        1: {"input": {"Temperature": 20, "Humidity": 50, "wind_speed": 10, "rain_probability": 10}, "expected": 1},  # Все ок
        2: {"input": {"Temperature": 40, "Humidity": 50, "wind_speed": 10, "rain_probability": 10}, "expected": 0},  # Температура слишком высокая
        3: {"input": {"Temperature": 20, "Humidity": 80, "wind_speed": 10, "rain_probability": 10}, "expected": 0},  # Влажность слишком высокая
        4: {"input": {"Temperature": 20, "Humidity": 50, "wind_speed": 60, "rain_probability": 10}, "expected": 0},  # Скорость ветра слишком высокая
        5: {"input": {"Temperature": 20, "Humidity": 50, "wind_speed": 10, "rain_probability": 40}, "expected": 0},  # Вероятность дождя слишком высокая
    }

    for test_number, test in tests.items():
        result = check_bad_weather(test["input"])
        assert result == test["expected"], f"Test {test_number} failed: expected {test['expected']}, got {result}"
        print(f"Test {test_number} passed.")
        
  
test_weather_conditions()