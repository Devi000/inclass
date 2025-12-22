people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
hello_4map = map(lambda s: f"hello {len(s) <= 4}", people)
print(list(hello_4map))