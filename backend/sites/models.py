from django.db import models

# Create your models here.

class Site(models.Model):
    site_name = models.CharField(max_length=255)

    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)

    area_sqm = models.IntegerField()
    solar_irradiance_kwh = models.DecimalField(max_digits=4, decimal_places=2)
    grid_distance_km = models.DecimalField(max_digits=5, decimal_places=2)
    slope_degrees = models.DecimalField(max_digits=4, decimal_places=2)
    road_distance_km = models.DecimalField(max_digits=5, decimal_places=2)
    elevation_m = models.IntegerField()

    land_type = models.CharField(max_length=50)
    region = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name




class AnalysisResult(models.Model):
    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE,
        related_name='analysis_results'
    )

    solar_irradiance_score = models.DecimalField(max_digits=5, decimal_places=2)
    area_score = models.DecimalField(max_digits=5, decimal_places=2)
    grid_distance_score = models.DecimalField(max_digits=5, decimal_places=2)
    slope_score = models.DecimalField(max_digits=5, decimal_places=2)
    infrastructure_score = models.DecimalField(max_digits=5, decimal_places=2)

    total_suitability_score = models.DecimalField(max_digits=5, decimal_places=2)
    parameters_snapshot = models.JSONField()

    analysis_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-analysis_timestamp']
