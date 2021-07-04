import wolframalpha
API_Key ='94Q5XV-44YXV3KR3A'
client = wolframalpha.Client(API_Key)

def math(equation):
  res = client.query(equation.strip(),params=(("format","image,plaintext"),))
  print(res)
math('∫√cotx')