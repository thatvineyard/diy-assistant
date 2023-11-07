import openai
from datetime import datetime
import json

from components.utils.chathistory import ChatHistory

class ChatSession:

  def __init__(self, apiKey: str, history_directory: str):
    openai.api_key = apiKey
    self.chat_start_time = datetime.now()
    self.history = ChatHistory()

  def chat(self, question):
      # Provide the model name or ID
      # model = 'gpt-3.5-turbo'
      model = 'gpt-3.5-turbo-0613'

      system_prompt = open('components/system-prompts/system-prompt.txt', "r").read()
      history_prompt = self.history.toHistoryPrompt()
      pre_question_prompt = "Respond to the following: "

      full_system_prompt = system_prompt + history_prompt + pre_question_prompt

      # Generate a chat completion
      response = openai.ChatCompletion.create(
          model=model,
          messages=[
              {"role": "system", "content": full_system_prompt},
              {"role": "user", "content": question}
          ]
      )

      # Retrieve and return the generated response
      answer = response.choices[0].message.content.strip()
      
      self.history.saveChatRound(question, answer)
      
      return answer
