import csv
from django.core.management.base import BaseCommand
from accounts.models import StaffRegistry  # Make sure this is correct


class Command(BaseCommand):
    help = 'Import staff data from a CSV file'

   

    def handle(self, *args, **kwargs):
        file_path = "C:/Users/hp/Documents/devProjects/data/userData.csv"  # Adjust path as needed
        self.import_staff_from_csv(file_path)

    def import_staff_from_csv(self, file_path):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                staff_number = row['staff_number']
                full_name = row['full_name']
                is_used = row['is_used'].strip().lower() in ['true', '1', 'yes']

                obj, created = StaffRegistry.objects.update_or_create(
                    staff_number=staff_number,
                    defaults={
                        'full_name': full_name,
                        'is_used': is_used
                    }
                )
                self.stdout.write(f"{'Created' if created else 'Updated'}: {staff_number}")
