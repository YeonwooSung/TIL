import pgeocode


dist = pgeocode.GeoDistance('fr')
print(dist.query_postal_code("75013", "69006"))
print(dist.query_postal_code(["75013", "75014", "75015"], ["69006", "69005", "69004"]))
