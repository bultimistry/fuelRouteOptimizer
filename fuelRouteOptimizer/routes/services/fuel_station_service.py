from geopy.geocoders import Nominatim
from geopy.distance import geodesic

from routes.models import FuelStation


class FuelStationService:

    geolocator = Nominatim(
        user_agent="fuel_optimizer"
    )


    @staticmethod
    def geocode_station(station):

        full_address = (
            f"{station.address}, "
            f"{station.city}, "
            f"{station.state}"
        )

        try:

            location = (
                FuelStationService
                .geolocator
                .geocode(full_address)
            )

            if location:

                return (
                    location.latitude,
                    location.longitude
                )

        except Exception:

            return None

        return None


    @staticmethod
    def find_nearby_stations(
        route_points,
        radius_miles=10
    ):

        nearby_stations = []

        stations = FuelStation.objects.all()[:300]

        for station in stations:

            station_coords = (
                FuelStationService
                .geocode_station(station)
            )

            if not station_coords:
                continue

            for point in route_points:

                distance = geodesic(
                    point,
                    station_coords
                ).miles

                if distance <= radius_miles:

                    nearby_stations.append({
                        "station": station,
                        "distance": distance
                    })

                    break

        return nearby_stations