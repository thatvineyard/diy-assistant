from typing import Callable

CBLUE2   = '\33[94m'
CEND = '\033[0m'

class Assistance:
  
  def __init__(self):
    self.actions: list[tuple[Callable[[], None]], str] = []
  
  def addAction(self, callback: Callable[[], None], description: str):
    self.actions.append((callback,description))
  
  def execute(self):
    for action in self.actions:
      print(f'{CBLUE2}ASSISTANCE: {action[1]}{CEND}')
      action[0]()