from dotenv import load_dotenv

load_dotenv()

from routes.services.geocoding_service import (
    GeocodingService
)

from routes.services.routing_service import (
    RoutingService
)


start = GeocodingService.get_coordinates(
    "New York"
)

end = GeocodingService.get_coordinates(
    "Chicago"
)

print("START:", start)

print("END:", end)

route = RoutingService.get_route(
    start,
    end
)

print(route)