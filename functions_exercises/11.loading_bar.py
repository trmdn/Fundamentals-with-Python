def loading_bar(char):
    if char == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    if char != 100:
        load_percent = char // 10
        return f"{char}% [{'%' * load_percent}{'.' * (10 - load_percent)}]\nStill loading..."


number = int(input())
print(loading_bar(number))
