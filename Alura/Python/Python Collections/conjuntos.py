usuarios_data_science = [15, 23, 43 ,56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)

print(set(assistiram))


for usuario in set(assistiram):
    print(usuario)

usuarios_data_science = {15, 23, 43 ,56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_data_science | usuarios_machine_learning)
print(usuarios_data_science & usuarios_machine_learning)
print(usuarios_data_science - usuarios_machine_learning)
print(usuarios_data_science ^ usuarios_machine_learning)

usuarios = {1, 5, 76, 34, 52, 13, 17}

usuarios_ice = frozenset(usuarios)

