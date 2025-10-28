import data_fetcher


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
    name = input("Enter a name of an animal: ").strip()
    if not name:
        print("No animal provided. Abort.")
        return

    animals_data = data_fetcher.fetch_animals(name)
    if not animals_data:
        message = f'<h2>The animal "{name}" doesn\'t exist.</h2>'

        with open('animals_template.html', 'r', encoding='utf-8') as f:
            template = f.read()

        updated_html = template.replace('__REPLACE_ANIMALS_INFO__', message)
        updated_html = updated_html.replace('<head>', '<head>\n        <meta charset="UTF-8">')

        with open('animals.html', 'w', encoding='utf-8') as f:
            f.write(updated_html)

        print(f'No results found for "{name}". Message written to animals.html.')
        return

    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)

    with open('animals_template.html', 'r', encoding='utf-8') as f:
        animals_html_text = f.read()

    print("Website was successfully generated to the file animals.html.")

    updated_html = animals_html_text.replace('__REPLACE_ANIMALS_INFO__', output)

    # Ensures the HTML file declares UTF-8 encoding to prevent character display issues
    updated_html = updated_html.replace('<head>', '<head>\n        <meta charset="UTF-8">')

    with open('animals.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)


if __name__ == "__main__":
    main()
