import urwid
import re


password = input()


def has_digit(password):
   return any(bukvitsa.isdigit() for bukvitsa in password)


def has_letters(password):
   return any(bukvitsa.isalpha() for bukvitsa in password)


def is_very_long(password):
    return any(len(password) > 12 for bukvitsa in password)


def has_upper_letters(password):
 for bukvitsa in password:
  if bukvitsa.isupper():
   return any(bukvitsa for bukvitsa in password)


def has_lower_letters(password):
    return any(bukvitsa.isupper() for bukvitsa in password)


def has_symbols(password):
    return bool(re.search(r"[@^%&*]", password))

def main():
  def on_ask_change(edit, new_edit_text):
      score = 0
      criteria = [
          lambda p: len(p) > 12,  
          lambda p: any(char.isdigit() for char in p), 
          lambda p: any(char.isalpha() for char in p),  
          lambda p: any(char.islower() for char in p), 
          lambda p: any(char.isupper() for char in p),  
          lambda p: bool(re.search(r"[@^%&*]", p))  
      ]
      for criterion in criteria:
          if criterion(new_edit_text):
              score += 2
      reply.set_text(f"Оценка пароля: {score}")
  ask = urwid.Edit('Введите пароль: ', mask='*')
  reply = urwid.Text("")
  menu = urwid.Pile([ask, reply])
  menu = urwid.Filler(menu, valign='top')
  urwid.connect_signal(ask, 'change', on_ask_change)
  urwid.MainLoop(menu).run()
if __name__ == "__main__":
  main()



























