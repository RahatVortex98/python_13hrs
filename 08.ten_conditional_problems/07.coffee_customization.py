# Customize a coffee order:"Small","Medium",or "Large" with an option for "Extra shot" of espresso




coffee_size =input('what size u want ?(Small/Medium/Large) :')
extra_shot = input('Do u need extra shot? :(Yes/No) ')

order = f"{coffee_size} coffee"


if extra_shot.lower() == 'yes':
    order += 'With an extra shot of espresso'

print(f"Your order:{order}")