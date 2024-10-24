from utils import weather_citykey, geoposition_Search

  
def main(coord): # функция, которая выполняет задание
  citykey = geoposition_Search(coord)
  if citykey == 0:
    print("Ошибка")
    return 0
  weather = weather_citykey(citykey)
  if weather == 0:
    print("Ошибка")
    return 0
  print(f"Температура: {weather['Temperature']:.1f} °C")
  print(f"Влажность: {weather['Humidity']}%")
  print(f"Скорость ветра: {weather['wind_speed']} hm/h")
  print(f"Вероятность дождя: {weather['rain_probability']}%")


if __name__ == "__main__":
  coord = input("Введите свои координаты (или просто Enter) \n> ")
  if coord == "":
    coord = "55.89751434326172, 37.55717468261719"
  main(coord)
