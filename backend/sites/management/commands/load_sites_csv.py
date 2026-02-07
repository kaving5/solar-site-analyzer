


import csv
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from sites.models import Site


class Command(BaseCommand):
    help = "Load solar site data from a CSV file into the Site table"

    # Required CSV columns for validations
    REQUIRED_COLUMNS = {
        'site_name',
        'latitude',
        'longitude',
        'area_sqm',
        'solar_irradiance_kwh',
        'grid_distance_km',
        'slope_degrees',
        'road_distance_km',
        'elevation_m',
        'land_type',
        'region'
    }

    def add_arguments(self, parser):
        parser.add_argument(
            'csv_file',
            type=str,
            help='Absolute or relative path to the CSV file'
        )

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        self.stdout.write(self.style.NOTICE(
            f"Starting CSV import from: {csv_file_path}"
        ))

        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)

                # Validate CSV headers
                if not reader.fieldnames:
                    raise CommandError("CSV file has no headers")

                missing_columns = self.REQUIRED_COLUMNS - set(reader.fieldnames)
                if missing_columns:
                    raise CommandError(
                        f"CSV is missing required columns: {missing_columns}"
                    )

                created_count = 0
                skipped_count = 0

                # Process rows Correctly
                for row_number, row in enumerate(reader, start=2):
                    try:
                        with transaction.atomic():
                            Site.objects.create(
                                site_name=row['site_name'].strip(),
                                latitude=row['latitude'],
                                longitude=row['longitude'],
                                area_sqm=row['area_sqm'],
                                solar_irradiance_kwh=row['solar_irradiance_kwh'],
                                grid_distance_km=row['grid_distance_km'],
                                slope_degrees=row['slope_degrees'],
                                road_distance_km=row['road_distance_km'],
                                elevation_m=row['elevation_m'],
                                land_type=row['land_type'].strip(),
                                region=row['region'].strip()
                            )
                            created_count += 1

                    except Exception as e:
                        skipped_count += 1
                        self.stderr.write(
                            f"Row {row_number} skipped due to error: {e}"
                        )

        except FileNotFoundError:
            raise CommandError(f"CSV file not found: {csv_file_path}")

        except Exception as e:
            raise CommandError(f"Failed to load CSV: {e}")


        self.stdout.write(self.style.SUCCESS(
            f"CSV import completed. "
            f"Created: {created_count}, Skipped: {skipped_count}"
        ))
