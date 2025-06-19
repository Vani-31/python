rivers={
    'nile':'egypt',
    'ganga':'india',
    'yamuna':'india' ,
    
}
for river , country in rivers.items():
    print(f"The {river} runs through {country}.")

for river in set(rivers.keys()):
    print(river.title())

print("\n")
for country in set(rivers.values()):
    print(country.title())