# Daffodil plant file for testing Plant creation

from app_plants import Daffodil

daffodil = Daffodil("daffodil", "yellow", 2, "Europe")
print(daffodil)
print(daffodil.plant_info())
print(daffodil.lifestyle())
daffodil.is_your_birthday()
print("\nNow the plant has aged.\n")
print(daffodil.plant_info())
