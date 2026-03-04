from traffic_light import TrafficLight

if __name__ == '__main__':
  light = TrafficLight()

  light.show_stats()      

  light.timer_red()
  light.timer_red_yellow()

  light.show_stats()      

  light.timer_green()
  light.timer_yellow()
  light.night_mode_on()
  light.timer_red()

  light.show_stats()      

  light.night_mode_off()
  light.timer_green()
  light.timer_red()

  light.show_stats()