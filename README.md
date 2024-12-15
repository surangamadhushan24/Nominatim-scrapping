# CafeScraperBot

CafeScraperBot is a simple web scraping project built using Scrapy. It scrapes cafe information from OpenStreetMap's Nominatim API for Colombo, Sri Lanka.

## Features
- Scrapes cafe names, latitude, and longitude.
- Fetches up to 50 results per request.
- Simple and lightweight.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cafescraperbot.git
   cd cafescraperbot
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install scrapy
   ```

## Usage
1. Run the spider using Scrapy:
   ```bash
   scrapy crawl cafespider -o cafes.json
   ```
2. Check the generated `cafes.json` file for results.

## Output Format
The output JSON file contains:
```json
[
  {
    "name": "Cafe Name, Full Address",
    "latitude": "6.927079",
    "longitude": "79.861244"
  }
]
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer
This project is for educational purposes only. Be respectful when scraping public APIs and ensure compliance with their terms of service.

