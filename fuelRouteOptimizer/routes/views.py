from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services.geocoding_service import (
    GeocodingService
)

from .services.routing_service import (
    RoutingService
)

from .services.optimization_service import (
    OptimizationService
)


def home(request):

    return render(
        request,
        "index.html"
    )


class RouteAPIView(APIView):

    def post(self, request):

        try:

            start_location = request.data.get(
                "start"
            )

            end_location = request.data.get(
                "finish"
            )

            if not start_location or not end_location:

                return Response(
                    {
                        "error":
                        "Start and finish are required"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Get coordinates
            start_coords = (
                GeocodingService.get_coordinates(
                    start_location
                )
            )

            end_coords = (
                GeocodingService.get_coordinates(
                    end_location
                )
            )

            # Get route
            route_data = (
                RoutingService.get_route(
                    start_coords,
                    end_coords
                )
            )

            route = route_data["routes"][0]

            distance_meters = (
                route["summary"]["distance"]
            )

            duration_seconds = (
                route["summary"]["duration"]
            )

            distance_miles = (
                OptimizationService
                .meters_to_miles(
                    distance_meters
                )
            )

            # SIMPLE FAST VERSION
            fuel_plan = (
                OptimizationService
                .build_fuel_plan(
                    distance_miles
                )
            )

            return Response({

                "start":
                    start_location,

                "finish":
                    end_location,

                "route_summary": {

                    "distance_miles":
                        round(distance_miles, 2),

                    "duration_seconds":
                        duration_seconds
                },

                "fuel_plan":
                    fuel_plan,

                "route_geometry":
                    route["geometry"]
            })

        except Exception as e:

            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )