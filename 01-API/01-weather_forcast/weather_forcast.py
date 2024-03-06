import requests
import arcade
from weather_icon import Sunny
from weather_icon import Cloudy
from weather_icon import Rainy
from weather_icon import Snowy





class Weather(arcade.Window):
    def __init__(self):
        super().__init__(width=400, height=400, title="Weather Forcast")
        arcade.set_background_color(arcade.color.PURPLE)
        # self.cloudy = Cloudy()
        # self.sunny = Sunny()
        # self.rainy = Rainy()
        # self.snowy = Snowy()
        self.weather_icon = None
        self.city_input =""

    def fetch_weather(self):
        city = self.city_input.lower()  # City for weather forecast
        url = f'https://goweather.herokuapp.com/weather/{city}'
        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()
            weather_description = weather_data['description']

            if 'sunny' in weather_description.lower():
                self.weather_icon = Sunny()
            elif 'cloudy' in weather_description.lower():
                self.weather_icon = Cloudy()
            elif 'rain' in weather_description.lower():
                self.weather_icon = Rainy()
            elif 'snow' in weather_description.lower():
                self.weather_icon = Snowy()
            # else:
            #     self.weather_icon = DefaultWeatherIcon()
            
            self.temperature = weather_data['temperature']
            self.wind = weather_data['wind']
            print(f"The current weather in {city} is {weather_description} with a temperature of {self.temperature} and wind speed of {self.wind}.")
        else:
            print("Failed to fetch weather data.")


    def on_draw(self):
        arcade.start_render()

        if self.weather_icon:
            self.weather_icon.draw()
            self.draw_temperatur()

        arcade.draw_text("Enter city:", 20, self.height - 50, arcade.color.WHITE, font_size=15)
        arcade.draw_text(self.city_input, 120, self.height - 50, arcade.color.WHITE, font_size=15)

    def on_update(self, delta_time: float):
        ...


    def draw_temperatur(self):
        output = f"Wind: {self.wind}   temperature {self.temperature} ."
        
        arcade.draw_text(output, 100 , 100, arcade.color.WHITE, 10 )
  

    def on_key_press(self, key, modifiers):
        if key == arcade.key.BACKSPACE:
            self.city_input = self.city_input[:-1]
        elif key == arcade.key.ENTER:
            self.fetch_weather()
        else:
            self.city_input += chr(key)


if __name__ == "__main__":
    weather = Weather()
    arcade.run()