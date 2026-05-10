import os
import requests

ORS_API_KEY = os.getenv("ORS_API_KEY")


class GeocodingService:

    BASE_URL = (
        "https://api.openrouteservice.org/geocode/search"
    )

    @staticmethod
    def get_coordinates(place):

        headers = {
            "Authorization": ORS_API_KEY
        }

        params = {
            "text": place,
            "size": 1
        }

        response = requests.get(
            GeocodingService.BASE_URL,
            headers=headers,
            params=params
        )

        response.raise_for_status()

        data = response.json()

        features = data.get("features")

        if not features:
            raise Exception("Location not found")

        coordinates = (
            features[0]["geometry"]["coordinates"]
        )

        return coordinates