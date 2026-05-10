import pandas as pd

from django.core.management.base import BaseCommand

from routes.models import FuelStation


class Command(BaseCommand):
    help = "Import fuel station data"


    def handle(self, *args, **kwargs):

        df = pd.read_csv(
            "data/fuel-prices-for-be-assessment.csv"
        )

        FuelStation.objects.all().delete()

        stations = []

        for _, row in df.iterrows():

            station = FuelStation(
                opis_truckstop_id=row["OPIS Truckstop ID"],
                truckstop_name=row["Truckstop Name"],
                address=row["Address"],
                city=row["City"],
                state=row["State"],
                rack_id=row["Rack ID"],
                retail_price=row["Retail Price"],
            )

            stations.append(station)

        FuelStation.objects.bulk_create(stations)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully imported {len(stations)} fuel stations"
            )
        )