class TrafficLight:
  # States
  __X0 = "Red"
  __X1 = "Red Yellow"
  __X2 = "Green"
  __X3 = "Yellow" 
  __X4 = "Flash Yellow"
  
  # In signals
  __U = [
    "Timeout R",
    "Timeout RY",
    "Timeout G",
    "Timeout Y", 
    "Night mode on", 
    "Night mode off"
  ]

  # Out signals
  __Y0 = False # Red is on
  __Y1 = False # Yellow is on
  __Y2 = False # Green is on
  __Y3 = False # Flash Yellow is on

  def __init__(self):
    self.__current_x = self.__X0
    self.__update_out_signals()

    self.__transitions = {
      (self.__X0, self.__U[0]): self.__X1,
      (self.__X1, self.__U[1]): self.__X2,
      (self.__X2, self.__U[2]): self.__X3,
      (self.__X3, self.__U[3]): self.__X0,

      (self.__X0, self.__U[4]): self.__X4,
      (self.__X1, self.__U[4]): self.__X4,
      (self.__X2, self.__U[4]): self.__X4,
      (self.__X3, self.__U[4]): self.__X4,

      (self.__X4, self.__U[5]): self.__X0,
    }

  def __update_out_signals(self):
    match self.__current_x:
      case self.__X0:
        self.__Y0, self.__Y1, self.__Y2, self.__Y3 = True, False, False, False
      case self.__X1:
        self.__Y0, self.__Y1, self.__Y2, self.__Y3 = True, True, False, False
      case self.__X2:
        self.__Y0, self.__Y1, self.__Y2, self.__Y3 = False, False, True, False
      case self.__X3:
        self.__Y0, self.__Y1, self.__Y2, self.__Y3 = False, True, False, False
      case self.__X4:
        self.__Y0, self.__Y1, self.__Y2, self.__Y3 = False, False, False, True
  
  def __apply_event(self, event_num):
    key = (self.__current_x, self.__U[event_num])

    print(f"Signal: '{self.__U[event_num]}'")

    if key in self.__transitions:
      new_x = self.__transitions[key]
      self.__current_x = new_x
      self.__update_out_signals()
    else:
      print("! was ignored")

  # Public methods that give In signals
  def timer_red(self):
    self.__apply_event(0)

  def timer_red_yellow(self):
    self.__apply_event(1)
  
  def timer_green(self):
    self.__apply_event(2)

  def timer_yellow(self):
    self.__apply_event(3)

  def night_mode_on(self):
    self.__apply_event(4)
  
  def night_mode_off(self):
    self.__apply_event(5)

  def show_stats(self):
    print(f"Current state: {self.__current_x}\n"
    f"Flags: R={int(self.__Y0)}, Y={int(self.__Y1)}, G={int(self.__Y2)}, FY={int(self.__Y3)}")