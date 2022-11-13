from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Company
from .serializer import CompanySerializer

class CompanyView(APIView):

    def get_all(self, request):
        serializer = CompanySerializer(Company.objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request):
        company = Company.objects.get(company_name = request.data.get('company_name'))
        layoff_count = request.data.get('layoff_count')

        if company:
            layoff_count += company.layoff_count 
        
        data = {
            'company_name': request.data.get('company_name'), 
            'layoff_count': layoff_count, 
            'id': request.user.id
        }
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

