import wolframalpha
API_Key =''
client = wolframalpha.Client(API_Key)

def math(equation):
  res = client.query(equation.strip(),params=(("format","image,plaintext"),))
  print(res)
math('∫√cotx')