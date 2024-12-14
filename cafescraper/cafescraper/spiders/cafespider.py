import scrapy


class CafeSpider(scrapy.Spider):
    name = "cafespider"

    def start_requests(self):
        # URL with query parameters for cafes in Colombo, Sri Lanka
        url = "https://nominatim.openstreetmap.org/search?q=cafe,Colombo,Sri+Lanka&format=json&addressdetails=1&limit=50"

        # Set headers to avoid getting blocked by the website
        headers = {
            "User-Agent": "CafeScraperBot/1.0 (+https://www.madhushan.com)"
        }

        # Make the request and pass the callback method for parsing the response
        yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        try:
            # Parse the JSON response
            cafes = response.json()

            # Extract details for each cafe
            for cafe in cafes:
                yield {
                    "name": cafe.get("display_name"),
                    "latitude": cafe.get("lat"),
                    "longitude": cafe.get("lon")
                }
        except Exception as e:
            self.logger.error(f"Parsing error: {e}")
