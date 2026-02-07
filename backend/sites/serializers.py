

from rest_framework import serializers
from sites.models import Site
from sites.services.suitability_calculator import SuitabilityCalculator

class SiteListSerializer(serializers.ModelSerializer):
    total_score = serializers.FloatField()

    class Meta:
        model = Site
        fields = [
            'id',
            'site_name',
            'latitude',
            'longitude',
            'total_score'
        ]

class SiteDetailSerializer(serializers.ModelSerializer):
    scores = serializers.SerializerMethodField()
    total_score = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Site
        fields = [
            'id',
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
            'region',
            'scores',
            'total_score',
            'category'
        ]

    def get_scores(self, obj):
        calculator = SuitabilityCalculator()
        _, scores = calculator.calculate(obj)
        return scores

    def get_total_score(self, obj):
        calculator = SuitabilityCalculator()
        total, _ = calculator.calculate(obj)
        return round(total, 2)

    def get_category(self, obj):
        calculator = SuitabilityCalculator()
        total, _ = calculator.calculate(obj)
        return SuitabilityCalculator.category(total)


class GetSiteByIdRequestSerializer(serializers.Serializer):
    site_id = serializers.IntegerField()

    def validate(self, attrs):
        # reject extra fields
        if set(self.initial_data.keys()) != {"site_id"}:
            raise serializers.ValidationError(
                "Only 'site_id' field is allowed"
            )
        return attrs

    def validate_site_id(self, value):
        if not Site.objects.filter(id=value).exists():
            raise serializers.ValidationError(
                f"Site with id {value} does not exist"
            )
        return value
    

class AnalyzeRequestSerializer(serializers.Serializer):
    weights = serializers.DictField()

    REQUIRED_KEYS = {
        "solar",
        "area",
        "grid",
        "slope",
        "infrastructure"
    }

    def validate(self, attrs):
        weights = attrs.get("weights")

        # Only 'weights' allowed at root
        if set(self.initial_data.keys()) != {"weights"}:
            raise serializers.ValidationError(
                "Only 'weights' field is allowed"
            )

        # Validate keys
        if set(weights.keys()) != self.REQUIRED_KEYS:
            raise serializers.ValidationError(
                f"weights must contain exactly {self.REQUIRED_KEYS}"
            )

        # Validate values
        total = 0
        for key, value in weights.items():
            if not isinstance(value, (int, float)):
                raise serializers.ValidationError(
                    f"{key} must be a number"
                )
            if value < 0 or value > 1:
                raise serializers.ValidationError(
                    f"{key} must be between 0 and 1"
                )
            total += value

        if abs(total - 1.0) > 0.001:
            raise serializers.ValidationError(
                "Sum of all weights must be exactly 1.0"
            )

        return attrs

