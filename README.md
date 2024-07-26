# animal-facts

Animal Facts is a web application that allows users to search for various animals and get quick facts about them. The application uses the API Ninjas Animals API to fetch animal data and provides a Google Images search link for further exploration.

## Features

- Search for animals by name
- Display quick facts about the animal including habitat, diet, lifespan, and more
- Provide a link to Google Images for viewing more images of the animal
- Responsive design with a loading spinner to indicate search progress

## Technologies Used

- Python
- Flask
- HTML
- CSS (Bootstrap, Google Fonts)
- JavaScript

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository

   ```sh
   git clone https://github.com/Black-Scorpio/animal-facts.git
   cd animal-facts

2. Create and activate a virtual enviornment
    ```python
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. Install required packages
    ```pip
   pip install Flask python-dotenv requests

4. Create a .env file and add your API key
    ```touch
   touch .env
   Add the following to the .env file
   API_KEY=your_api_ninjas_key_here
   API key can be found from registering here https://api-ninjas.com/api/animals

5. Run the application
    ```python
   python app.py