import pgeocode

nomi = pgeocode.Nominatim('fr')
print(nomi.query_location("Antibes", top_k=3))
print(nomi.query_location("Straassborg", top_k=3, fuzzy_threshold=80))
