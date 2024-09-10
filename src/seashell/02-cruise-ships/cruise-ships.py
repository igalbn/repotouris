ships = [
    {
        "name": "Icon of the Seas",
        "gross_tonnage": 248663,
        "length": 364.75,
        
    },
    {
        "name": "Utopia of the Seas",
        "gross_tonnage": 236473,
        "length": 361.12
    },
    {
        "name": "Wonder of the Seas",
        "gross_tonnage": 235600,
        "length": 362.04
    },
    {
        "name": "Symphony of the Seas",
        "gross_tonnage": 228081,
        "length": 361.01
    },
    {
        "name": "Harmony of the Seas",
        "gross_tonnage": 226963,
        "length": 362.12
    }
]

print('Biggest five cruise ships\n')

for ship in ships:
    print('Name:', ship['name'])
    print('Gross Tonnage:', ship['gross_tonnage'])
    print('Length:', ship['length'])
    
    
    print('')

