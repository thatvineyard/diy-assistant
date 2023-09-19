import openai

class ChatSession:
  
  def __init__(self, apiKey: str):
    openai.api_key = apiKey

  def chat(self, question):
      # Provide the model name or ID
      # model = 'gpt-3.5-turbo'
      model = 'gpt-3.5-turbo-0613'

      system_prompt= open('components/system-prompts/system-prompt.txt', "r").read();

      # Generate a chat completion
      response = openai.ChatCompletion.create(
          model=model,
          messages=[
              {"role": "system", "content": system_prompt},
              {"role": "user", "content": question}
          ]
      )

      # Retrieve and return the generated response
      answer = response.choices[0].message.content.strip()
      return answer
