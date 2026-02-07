from rest_framework.views import APIView
from rest_framework.response import Response
from sites.models import Site
from sites.serializers import SiteListSerializer
from sites.services.suitability_calculator import SuitabilityCalculator
from rest_framework.generics import get_object_or_404
from sites.serializers import SiteDetailSerializer
from rest_framework import status

from rest_framework.decorators import api_view
from common.responses import success_response, error_response
from sites.serializers import GetSiteByIdRequestSerializer

from sites.serializers import AnalyzeRequestSerializer

#Function Based View (FBV) -- > 1 Option

#The below view can also be handled with Get Call (But I preferred Post)


@api_view(['POST'])
def get_site_by_id(request):
    serializer = GetSiteByIdRequestSerializer(data=request.data)

    if not serializer.is_valid():
        return error_response(
            message="Validation error",
            errors=serializer.errors
        )

    site = Site.objects.get(id=serializer.validated_data["site_id"])
    data = SiteDetailSerializer(site).data

    return success_response(
        data=data,
        message="Site fetched successfully"
    )



#Class Based View  ---> 2nd Option

class AnalyzeAPIView(APIView):
    def post(self, request):
        serializer = AnalyzeRequestSerializer(data=request.data)

        if not serializer.is_valid():
            return error_response(
                message="Validation error",
                errors=serializer.errors
            )

        weights = serializer.validated_data["weights"]
        calculator = SuitabilityCalculator(weights=weights)

        results = []
        for site in Site.objects.all():
            total, _ = calculator.calculate(site)
            results.append({
                "site_id": site.id,
                "site_name": site.site_name,
                "total_score": round(total, 2)
            })

        results.sort(key=lambda x: x["total_score"], reverse=True)

        return success_response(
            data={
                "weights_used": weights,
                "results": results
            },
            message="Analysis completed successfully"
        )
    
#Class Based View  
class SiteListAPIView(APIView):
    def get(self, request):
        calculator = SuitabilityCalculator()

        results = []
        for site in Site.objects.all():
            total, _ = calculator.calculate(site)
            results.append({
                'id': site.id,
                'site_name': site.site_name,
                'latitude': site.latitude,
                'longitude': site.longitude,
                'total_score': round(total, 2)
            })

        return success_response(
            data=results,
            message="Sites fetched successfully"
        )
    
#Class Based View  
class StatisticsAPIView(APIView):
    def get(self, request):
        calculator = SuitabilityCalculator()
        scores = []

        for site in Site.objects.all():
            total, _ = calculator.calculate(site)
            scores.append(total)

        if not scores:
            return success_response(
                data={},
                message="No sites available"
            )

        return success_response(
            data={
                "average_score": round(sum(scores) / len(scores), 2),
                "max_score": round(max(scores), 2),
                "min_score": round(min(scores), 2),
                "total_sites": len(scores)
            },
            message="Statistics fetched successfully"
        )
  
