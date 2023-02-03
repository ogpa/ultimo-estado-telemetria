l = ["a", "b", "c"]

# print(l.index("d"))
try:
    l.index("d")
    print("Hola")
except ValueError:
    print("No existe.")
