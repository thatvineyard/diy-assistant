import os
from pathlib import Path
import openai
from datetime import datetime

from components.utils.chat.chathistory import ChatHistory
from components.utils.chat.openai import OpenAiClient

class ChatSession:
  """A class used to chat with openAI and to keep track of the history."""
  
  def __init__(self, api_key: str, history_directory: str, history_file_path: str | None = None):
    
    self.openai_client = OpenAiClient(api_key)
    self.history = self.__getOrCreateChatHistory(history_directory, history_file_path)

  def chat(self, message):
      """Build a prompt, send to openAI and then save the history"""
      
      # Put together system prompt
      system_prompt = open('components/system-prompt.txt', "r").read()
      history_prompt = self.history.toHistoryPrompt()
      pre_question_prompt = "Respond to the following: "
      full_system_prompt = system_prompt + history_prompt + pre_question_prompt
      
      response = self.openai_client.generateChatCompletion(system_prompt=full_system_prompt, prompt=message)

      self.history.saveChatRound(message, response)
      
      return response

  def __getOrCreateChatHistory(self, history_directory: str, history_file_path: str | None = None):
      if history_file_path is not None:
        history_file_name = str(Path(history_file_path).relative_to(history_directory))
      else:
        history_file_name = f'{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.json'
      
      if os.path.exists(f'{history_directory}/{history_file_name}'):
        return ChatHistory.fromFile(history_directory, history_file_name)
      else:
        return ChatHistory(history_directory, history_file_name)