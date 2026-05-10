import math

from routes.models import FuelStation


class OptimizationService:

    VEHICLE_RANGE = 500

    MPG = 10


    @staticmethod
    def meters_to_miles(meters):

        return meters * 0.000621371


    @staticmethod
    def calculate_fuel_needed(distance_miles):

        return (
            distance_miles /
            OptimizationService.MPG
        )


    @staticmethod
    def calculate_total_stops(distance_miles):

        return math.ceil(
            distance_miles /
            OptimizationService.VEHICLE_RANGE
        )


    @staticmethod
    def build_fuel_plan(
        distance_miles
    ):

        fuel_needed = (
            OptimizationService
            .calculate_fuel_needed(
                distance_miles
            )
        )

        total_stops = (
            OptimizationService
            .calculate_total_stops(
                distance_miles
            )
        )

        nearby_stations = (
            FuelStation.objects
            .order_by("retail_price")
            [:total_stops]
        )

        fuel_stops = []

        total_cost = 0

        remaining_distance = distance_miles


        for station in nearby_stations:

            current_leg_distance = min(
                OptimizationService.VEHICLE_RANGE,
                remaining_distance
            )

            gallons_needed = (
                current_leg_distance /
                OptimizationService.MPG
            )

            stop_cost = (
                gallons_needed *
                station.retail_price
            )

            fuel_stops.append({

                "truckstop_name":
                    station.truckstop_name,

                "city":
                    station.city,

                "state":
                    station.state,

                "retail_price":
                    station.retail_price,

                "gallons_purchased":
                    round(gallons_needed, 2),

                "cost":
                    round(stop_cost, 2)
            })

            total_cost += stop_cost

            remaining_distance -= (
                current_leg_distance
            )

        return {

            "distance_miles":
                round(distance_miles, 2),

            "fuel_needed_gallons":
                round(fuel_needed, 2),

            "estimated_total_cost":
                round(total_cost, 2),

            "total_stops":
                total_stops,

            "fuel_stops":
                fuel_stops
        }