import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, 'r', encoding='utf-8') as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Converts an animal dictionary into an HTML list item string."""
    animal_name = animal_obj.get('name')
    animal_diet = animal_obj.get('characteristics').get('diet')
    animal_locations = ', '.join(list(animal_obj.get('locations')))
    animal_type = animal_obj.get('characteristics').get('type')
    animal_top_speed = animal_obj.get('characteristics').get('top_speed')

    output = ''
    output += '<li class="cards__item">'
    if animal_name:
        output += f'<div class="card__title">{animal_name}</div>\n'
    output += '<div class="card__text">\n<ul class="card__list">\n'
    if animal_diet:
        output += f'  <li class="card__list-item"><strong>Diet:</strong> {animal_diet}</li>\n'
    if animal_locations:
        output += f'  <li class="card__list-item"><strong>Location:</strong> {animal_locations}</li>\n'
    if animal_type:
        output += f'  <li class="card__list-item"><strong>Type:</strong> {animal_type}</li>\n'
    if animal_top_speed:
        output += f'  <li class="card__list-item"><strong>Top Speed:</strong> {animal_top_speed}</li>\n'
    output += '</ul>\n</div>\n</li>\n'

    return output


def main():
    """Generates an HTML file with animal information from a JSON data source."""
    animals_data = load_data('animals_data.json')

    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)

    with open('animals_template.html', 'r', encoding='utf-8') as f:
        animals_html_text = f.read()

    updated_html = animals_html_text.replace('__REPLACE_ANIMALS_INFO__', output)

    # Ensures the HTML file declares UTF-8 encoding to prevent character display issues
    updated_html = updated_html.replace('<head>', '<head>\n        <meta charset="UTF-8">')

    with open('animals.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)


if __name__ == "__main__":
    main()
