symvol_b = 4
stroka = symvol_b * 25
stranica = stroka * 50
kniga = stranica * 100

kalc = 1.44 * 1024 ** 2

pomest = kalc // kniga

print("Количество книг, помещающихся на дискету:", round(pomest))
