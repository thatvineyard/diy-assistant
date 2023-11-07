import os
import openai
from datetime import datetime
import json

from components.utils.chathistory import ChatHistory

class ChatSession:

  def __init__(self, apiKey: str, history_directory: str, history_file_name: str | None = None):
    
    # Set up OpenAI
    self.model = 'gpt-3.5-turbo-0613'
    openai.api_key = apiKey
    
    # Set up history file
    self.chat_start_time = datetime.now()
    
    if history_file_name is None:
      history_file_name = f'{self.chat_start_time.strftime("%d-%m-%Y_%H-%M-%S")}.json'
    
    if os.path.exists(f'{history_directory}/{history_file_name}'):
      self.history = ChatHistory.fromFile(history_directory, history_file_name)
    else:
      self.history = ChatHistory(history_directory, history_file_name)

  def chat(self, question):
      # Put together system prompt
      system_prompt = open('components/system-prompts/system-prompt.txt', "r").read()
      history_prompt = self.history.toHistoryPrompt()
      pre_question_prompt = "Respond to the following: "

      full_system_prompt = system_prompt + history_prompt + pre_question_prompt

      # Generate a chat completion
      response = openai.ChatCompletion.create(
          model=self.model,
          messages=[
              {"role": "system", "content": full_system_prompt},
              {"role": "user", "content": question}
          ]
      )

      # Retrieve, save and return the generated response
      answer = response.choices[0].message.content.strip()
      self.history.saveChatRound(question, answer)
      
      return answer
