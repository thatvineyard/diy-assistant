from typing import Callable
from colorama import Fore, Style

class Assistance:
  """
  An Assistance is a list of actions that can be executed by the assistant.
  Fill it by running `addAction(callback, description)`.
    For example: `assistance.addAction(lambda : print("Hello World"), "Print message")`
  Then execute all the actions sequentially by running `execute()`.
  """
  
  def __init__(self):
    self.actions: list[tuple[Callable[[], None]], str] = []
  
  def addAction(self, callback: Callable[[], None], description: str):
    self.actions.append((callback,description))
  
  def execute(self):
    for action in self.actions:
      print(f'{Fore.LIGHTBLUE_EX}ASSISTANCE:{Style.RESET_ALL} {action[1]}')
      action[0]()