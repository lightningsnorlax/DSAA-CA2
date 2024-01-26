from Classes.general import General

operators = ["**", "*", "/", "+", "-"]
new_pattern = r"(\(|\)|"
for i in operators:
    for char in i:
        new_pattern += f"\\{char}"
    new_pattern += "|"
new_pattern += r"\d+)"
print(new_pattern)
pattern = r"(\(|\)|\+|\-|\*\*|\*|\/|\d+)"
print(new_pattern)