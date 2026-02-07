


class SuitabilityCalculator:
    DEFAULT_WEIGHTS = {
        'solar': 0.35,
        'area': 0.25,
        'grid': 0.20,
        'slope': 0.15,
        'infrastructure': 0.05,
    }

    def __init__(self, weights=None):
        self.weights = weights or self.DEFAULT_WEIGHTS
        self._validate_weights()

    #Validation

    def _validate_weights(self):
        total = sum(self.weights.values())
        if abs(total - 1.0) > 0.001:
            raise ValueError(f"Weights must sum to 1.0, got {total}")

        for key, value in self.weights.items():
            if value < 0 or value > 1:
                raise ValueError(f"Invalid weight for {key}: {value}")

    # Individual Scores 
    def solar_score(self, value):
        if value >= 5.5:
            return 100.0
        elif value < 3.0:
            return 0.0
        return ((value - 3.0) / 2.5) * 100

    def area_score(self, value):
        if value >= 50000:
            return 100.0
        elif value < 5000:
            return 0.0
        return ((value - 5000) / 45000) * 100

    def grid_score(self, value):
        if value <= 1:
            return 100.0
        elif value >= 20:
            return 0.0
        return 100 - ((value - 1) / 19) * 100

    def slope_score(self, value):
        if value <= 5:
            return 100.0
        elif value > 20:
            return 0.0
        elif value <= 15:
            return 100 - ((value - 5) / 10) * 50
        return 50 - ((value - 15) / 5) * 50

    def infrastructure_score(self, value):
        if value <= 0.5:
            return 100.0
        elif value >= 5:
            return 0.0
        return 100 - ((value - 0.5) / 4.5) * 100

    # Final Calculation 

    def calculate(self, site):
        scores = {
            'solar': self.solar_score(float(site.solar_irradiance_kwh)),
            'area': self.area_score(site.area_sqm),
            'grid': self.grid_score(float(site.grid_distance_km)),
            'slope': self.slope_score(float(site.slope_degrees)),
            'infrastructure': self.infrastructure_score(float(site.road_distance_km)),
        }

        total_score = sum(
            scores[key] * self.weights[key]
            for key in scores
        )

        return round(total_score, 2), scores

    #Category 

    @staticmethod
    def category(score):
        if score >= 80:
            return "Excellent"
        elif score >= 60:
            return "Good"
        elif score >= 40:
            return "Fair"
        elif score >= 20:
            return "Poor"
        return "Very Poor"
