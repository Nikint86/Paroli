import urwid


MIN_LENGTH = 12


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_letters(password):
    return any(char.isalpha() for char in password)


def is_long_enough(password):
    return len(password) >= MIN_LENGTH


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return any(not char.isalnum() for char in password)


def calculate_score(password):
    score = 0
    criteria = [
        is_long_enough,
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]
    for criterion in criteria:
        if criterion(password):
          score += 2
    return score


def on_ask_change(edit, new_edit_text):
    score = calculate_score(new_edit_text)
    reply.set_text(f'Оценка пароля: {score}')


if __name__ == '__main__':
    ask = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text('')
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()



























