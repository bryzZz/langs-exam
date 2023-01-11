from enum import Enum, auto


def isLetter(char: str):
  return ord(char) in range(97, 122)


class VAR_TYPES(Enum):
  INT = "int"


class TokenType(Enum):
  VAR_TYPE = VAR_TYPES
  VAR_NAME = auto()
  ASSIGN = auto()
  SEMI = auto()
  STAR = auto()
  AMPERSAND = auto()
  NUMBER = auto()
  EOL = auto()


class Token:
  def __init__(self, type: TokenType, value: str) -> None:
    self.type = type
    self.value = value

  def __str__(self) -> str:
    return f"Token {self.type}, {self.value}"


class LexerException(Exception):
  ...


class Lexer:
  def __init__(self, text: str):
    self.pos = 0
    self.text = text
    self.current_char = self.text[self.pos]

  def number(self) -> str:
    result = []

    while self.current_char != '' and self.current_char.isdigit() or self.current_char == '.':
      result.append(self.current_char)
      self.forward()

    return "".join(result)

  def var_type(self, expected_type: VAR_TYPES) -> str:
    result = []

    for char in expected_type.value:
      if char == self.current_char:
        result.append(self.current_char)
        self.forward()
      else:
        raise LexerException(f'Incorrect {expected_type.value} word')

    return "".join(result)

  def identifier(self) -> str:
    result = []

    while isLetter(self.current_char):
      result.append(self.current_char)
      self.forward()

    return "".join(result)

  def forward(self):
    self.pos += 1

    if self.pos == len(self.text):
      self.current_char = ''
    else:
      self.current_char = self.text[self.pos]

  def skip(self):
    while self.current_char != "" and self.current_char.isspace():
      self.forward()

  def next(self) -> Token:
    while self.current_char != '':
      if self.current_char.isspace():
        self.skip()
        continue

      for var_type in VAR_TYPES:
        if self.current_char == var_type.value[0]:
          return Token(TokenType.VAR_TYPE, self.var_type(var_type))

      if isLetter(self.current_char):
        return Token(TokenType.VAR_NAME, self.identifier())

      if self.current_char == "*":
        ch = self.current_char
        self.forward()
        return Token(TokenType.STAR, ch)

      if self.current_char == "&":
        ch = self.current_char
        self.forward()
        return Token(TokenType.AMPERSAND, ch)

      if self.current_char == ';':
        ch = self.current_char
        self.forward()
        return Token(TokenType.SEMI, ch)

      if self.current_char == '=':
        ch = self.current_char
        self.forward()
        return Token(TokenType.ASSIGN, ch)

      if self.current_char.isdigit():
        return Token(TokenType.NUMBER, self.number())

      raise LexerException(f'bad token {self.current_char}')
    return Token(TokenType.EOL, "")


text = 'int value = 10;\nint* ptr = &value;'

lexer = Lexer(text)

token = lexer.next()

while token.type != TokenType.EOL:
  print(token)
  token = lexer.next()
