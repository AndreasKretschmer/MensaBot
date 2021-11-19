allergen = ['Milch']
zusatzstoffe = ['Mononatriumglutamat']
label = ['vegan', 'vegetarisch', 'ohne Schwein', 'ohne Fisch', 'ohne Alkohol']

g = {
    'name': 'Pasta Carbonara',
    'zutaten': 'Makkeroni, Tomatensauce, Gewürze, Gouda',
    'preis': '2.00',
    'zusatzstoffe': [zusatzstoffe[0]],
    'allergene': [allergen[0]],
    'labels': [label[0], label[1], label[2], label[3], label[4]]
}

gerichte = [g, g, g]

dummy_speiseplan = {
    'standort': 'Mensa am Park',
    'datum': '19-11-2021',
    'gericht': gerichte
}