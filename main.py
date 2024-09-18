import urwid


password = input()


def proverka(password): 
  score = 0
  if is_very_long(password):
   score += 2

  if  has_digit(password):
   score += 2

  if has_letters(password):
   score += 2

  if has_lower_letters(password):
   score += 2

  if has_upper_letters(password):
   score += 2

  if has_symbols(password):
   score += 2
  return score



def has_digit(password):
 for bukvitsa in password:
  if bukvitsa.isdigit():
   return any(bukvitsa for bukvitsa in password)


def has_letters(password):
 for bukvitsa in password:
  if bukvitsa.isalpha():
   return any(bukvitsa for bukvitsa in password)


def is_very_long(password):
  if len(password) > 12:
    return any(bukvitsa for bukvitsa in password)


def has_upper_letters(password):
 for bukvitsa in password:
  if bukvitsa.isupper():
   return any(bukvitsa for bukvitsa in password)


def has_lower_letters(password):
 for bukvitsa in password:
  if bukvitsa.islower():
    return any(bukvitsa for bukvitsa in password)


def has_symbols(password):
  for bukvitsa in password:
      if bukvitsa in "@^%&*":
       return any(bukvitsa for bukvitsa in password)


def on_ask_change(edit, new_edit_text):
    score = proverka(new_edit_text)
    reply.set_text(f"Оценка пароля: {score}")
ask = urwid.Edit('Введите пароль: ', mask='*')
reply = urwid.Text("")
menu = urwid.Pile([ask, reply])
menu = urwid.Filler(menu, valign='top')
urwid.connect_signal(ask, 'change', on_ask_change)
urwid.MainLoop(menu).run()




























