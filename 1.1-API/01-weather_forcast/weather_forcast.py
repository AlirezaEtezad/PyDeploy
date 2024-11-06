import requests
import arcade
import arcade.gui as gui
from weather_icon import Sunny
from weather_icon import Cloudy
from weather_icon import Rainy
from weather_icon import Snowy
from shapely import speedups
print(speedups.available)


# class SearchButton(gui.UIFlatButton):
#     def __init__(self, center_x, center_y, callback):
#         super().__init__(
#             center_x=center_x,
#             center_y=center_y,
#             text="Search",
#             width=100,
#             height=40,
#             id=None,
#         )
#         self.callback = callback

    # def on_click(self):
    #     if self.callback:
    #         self.callback()

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
        self.search_box_width = 200
        self.search_box_height = 30
        self.search_box_x = 130
        self.search_box_y = self.height - 60    

        # self.search_button = SearchButton(
        #     center_x=self.width // 2,
        #     center_y=self.search_box_y - self.search_box_height - 50,
        #     callback=self.fetch_weather
        # )    

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
            
            if 'forecast' in weather_data:
                self.forecast = weather_data['forecast']
        else:
            print("Failed to fetch weather data.")


    def on_draw(self):
        arcade.start_render()

        if self.weather_icon:
            self.weather_icon.draw()
            self.draw_temperatur()
            self.draw_forecast()

        arcade.draw_text("Enter city:", 20, self.height - 50, arcade.color.WHITE, font_size=15)
       # arcade.draw_text(self.city_input, 120, self.height - 50, arcade.color.WHITE, font_size=15)

        arcade.draw_xywh_rectangle_filled(self.search_box_x, self.search_box_y, self.search_box_width, self.search_box_height, arcade.color.WHITE)
        arcade.draw_text(self.city_input, self.search_box_x + 10, self.search_box_y + 10, arcade.color.BLACK, font_size=15) 
        # self.search_button.draw() 
            




    def draw_forecast(self):
        x = 70
        y = self.height - 320
        arcade.draw_text("Next 3 days:", x, y, arcade.color.WHITE, font_size=12)
        y -= 20
        for day_data in self.forecast:
            day = day_data['day']
            temperature = day_data['temperature']
            wind = day_data['wind']
            output = f"Day {day}: Temperature: {temperature}, Wind: {wind}"
            arcade.draw_text(output, x, y, arcade.color.WHITE, font_size=10)
            y -= 20

    def on_update(self, delta_time: float):
        ...


    def draw_temperatur(self):
        output = f"Wind: {self.wind}   temperature {self.temperature} ."
        
        arcade.draw_text(output, 100 , 150, arcade.color.WHITE, 10, bold=True )
  

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