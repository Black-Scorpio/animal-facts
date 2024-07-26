import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)
api_key = os.getenv('API_KEY')


def get_animal_data(animal_name):
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        animal_data = response.json()
        if not animal_data:
            return None, "No data found for the specified animal."

        # Extract necessary information and set default values for missing data
        processed_data = []
        for animal_info in animal_data:
            taxonomy = animal_info.get('taxonomy', {})
            characteristics = animal_info.get('characteristics', {})

            animal_details = {
                "name": animal_info.get("name", "N/A"),
                "scientific_name": taxonomy.get("scientific_name", "N/A"),
                "habitat": characteristics.get("habitat", "N/A"),
                "diet": characteristics.get("diet", "N/A"),
                "lifespan": characteristics.get("lifespan", "N/A"),
                "top_speed": characteristics.get("top_speed", "N/A"),
                "weight": characteristics.get("weight", "N/A"),
                "height": characteristics.get("height", "N/A"),
                "locations": ", ".join(animal_info.get("locations", ["N/A"])),
                "google_images_link": get_google_images_link(animal_info)
            }
            processed_data.append(animal_details)

        return processed_data, None
    else:
        return None, f"Error: {response.status_code} {response.text}"


def get_google_images_link(animal_info):
    search_query = animal_info.get("scientific_name", animal_info["name"]).replace(" ", "+")
    return f"https://www.google.com/search?tbm=isch&q={search_query}"


@app.route('/', methods=['GET', 'POST'])
def index():
    animal_data = None
    error_message = None

    if request.method == 'POST':
        animal_name = request.form['animal_name']
        animal_data, error_message = get_animal_data(animal_name)

        if not animal_data and not error_message:
            error_message = f"No results found for '{animal_name}'."

    return render_template('index.html', animal_data=animal_data, error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True)
