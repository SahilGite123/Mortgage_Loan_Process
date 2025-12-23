import googlemaps
import os

class DataCollectorAgent:

    def collect_location_data(self, address):
        gmaps = googlemaps.Client(
            key=os.getenv("GOOGLE_MAPS_API_KEY")
        )

        result = gmaps.geocode(address)

        if not result:
            return {"error": "Location not found"}

        location = result[0]["geometry"]["location"]

        return {
            "formatted_address": result[0]["formatted_address"],
            "latitude": location["lat"],
            "longitude": location["lng"],
            "place_id": result[0]["place_id"]
        }
