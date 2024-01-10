from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Jabama
from .serializers import JabamaSerializer


@csrf_exempt
def JabamaApi(request, id=0):
    if request.method == 'GET':
        jabamas = Jabama.objects.all()
        jabama_serializer = JabamaSerializer(jabamas, many=True)
        return JsonResponse(jabama_serializer.data, safe=False)

    elif request.method == 'POST':
        jabama_data = JSONParser().parse(request)
        jabama_serializer = JabamaSerializer(data=jabama_data)
        if jabama_serializer.is_valid():
            jabama_serializer.save()
            return JsonResponse('Added successfully', safe=False)
        return JsonResponse({'error': 'Failed to add'}, status=400)

    elif request.method == 'PUT':
        jabama_instance = get_object_or_404(Jabama, pk=id)
        jabama_data = JSONParser().parse(request)
        jabama_serializer = JabamaSerializer(jabama_data, data=jabama_data)
        if jabama_serializer.is_valid():
            jabama_serializer.save()
            return JsonResponse('Updated successfully', safe=False)
        return JsonResponse({'error': 'Failed to update'}, status=400)
