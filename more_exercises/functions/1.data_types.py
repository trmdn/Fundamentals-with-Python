def data_types(current_command, type_of_el):
    if current_command == "int":
        type_of_el = int(type_of_el) * 2
        return type_of_el
    elif current_command == "real":
        type_of_el = float(type_of_el) * 1.5
        return f"{type_of_el:.2f}"
    elif current_command == "string":
        return f"${type_of_el}$"


command = input()
type_of_element = input()
result = data_types(command, type_of_element)
print(result)