from typing import Callable

class Assistance:
  
  def __init__(self):
    self.actions: list[tuple[Callable[[], None]], str] = []
  
  def addAction(self, callback: Callable[[], None], description: str):
    self.actions.append((callback,description))
  
  def execute(self):
    for action in self.actions:
      print(action[1])
      action[0]()