import json


class ChatRound:

  def __init__(self, question: str, response: str):
    self.question = question
    self.response = response
  
  def toPrompt(self):
    return f'''
    I asked: {self.question}
    You answered: {self.response}
    '''
    
class ChatHistory:
  
  def __init__(self, apiKey: str, history_directory: str):
    self.history: list[ChatRound] = []
    self.history_file_path = f'{history_directory}/{self.chat_start_time.strftime("%d-%m-%Y_%H-%M-%S")}.json'
  
  def saveChatRound(self, question: str, answer: str):
    chatRound = ChatRound(question, answer)
    self.history.append(chatRound)
    self.storeHistory()
    
  def _storeHistory(self):
    json_string = json.dumps(self.history, default=lambda o: o.__dict__, 
        sort_keys=True, indent=4)
    open(self.history_file_path, "w").write(json_string)
  
  def toHistoryPrompt(self):
    history_prompt = "Chat history:\n"
    for round in self.history:
      history_prompt += round.toPrompt()
    return history_prompt