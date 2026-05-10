import os
import requests

ORS_API_KEY = os.getenv("ORS_API_KEY")


class RoutingService:

    BASE_URL = (
        "https://api.openrouteservice.org/v2/directions/driving-car"
    )

    @staticmethod
    def get_route(start, 
                  end
                  ):

        headers = {
            "Authorization": ORS_API_KEY,
            "Content-Type": "application/json"
        }

        body = {
            "coordinates": [
                start,
                end
            ]
        } 

       


        response = requests.post(
            RoutingService.BASE_URL,
            json=body,
            headers=headers
        )

        response.raise_for_status()

        return response.json()