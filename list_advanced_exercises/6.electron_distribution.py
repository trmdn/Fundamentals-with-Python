electron = int(input())
electron_distribution = []

for electrons in range(1, electron + 1):
    max_electrons_in_current_shell = 2 * electrons ** 2
    if electron >= max_electrons_in_current_shell:
        electron_distribution.append(max_electrons_in_current_shell)
        electron -= max_electrons_in_current_shell
        if electron == 0:
            break
    else:
        electron_distribution.append(electron)
        break
print(electron_distribution)
