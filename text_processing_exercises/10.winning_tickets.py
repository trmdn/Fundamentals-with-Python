tickets = input().replace(" ", "")
tickets = tickets.split(',')
count = 0
symb = ''
symbols = ['@', '#', '$', '^']

for ticket in tickets:
    fins_ticket = False
    if len(ticket) != 20:
        print('invalid ticket')
        continue
    left = ticket[:int(len(ticket) / 2)]
    right = ticket[int(len(ticket) / 2):]
    for index, sym in enumerate(symbols):
        if 6 * sym in left and 6 * sym in right:
            count = 0
            for i in range(7, 11):
                if (i * sym) in left and (i * sym) in right:
                    count += 1
            symb = symbols[index]
            fins_ticket = True
    if not fins_ticket:
        print(f'ticket "{ticket}" - no match')
    elif count != 4:
        print(f'ticket "{ticket}" - {6 + count}{symb}')
    else:
        print(f'ticket "{ticket}" - {6 + count}{symb} Jackpot!')