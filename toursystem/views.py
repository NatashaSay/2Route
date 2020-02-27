from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

# from rest_framework.schemas.inspectors import AutoSchema
# from rest_framework.schemas.coreapi import AutoSchema

from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='API')


class InfoView(APIView):

    def get(self, request):
        route = Route.objects.all()
        routeserializer = RouteSerializer(route, many=True)
        return Response({"info":routeserializer.data})



def index(request):
    return render(request, 'index.html')
