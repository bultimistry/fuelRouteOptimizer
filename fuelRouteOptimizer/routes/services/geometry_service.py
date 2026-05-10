import polyline


class GeometryService:

    @staticmethod
    def decode_geometry(encoded_geometry):

        coordinates = polyline.decode(
            encoded_geometry
        )

        return coordinates


    @staticmethod
    def sample_route_points(
        coordinates,
        step=50
    ):

        return coordinates[::step]