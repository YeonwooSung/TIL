import pgeocode

nomi = pgeocode.Nominatim('fr')
print(nomi.query_postal_code("75013"))
print(nomi.query_postal_code(["75013", "69006"]))
