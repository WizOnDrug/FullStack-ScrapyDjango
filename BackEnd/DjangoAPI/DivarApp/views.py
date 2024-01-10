from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Divar
from .serializers import DivarSerializer


@csrf_exempt
def DivarApi(request, id=0):
    if request.method == 'GET':
        divars = Divar.objects.all()
        divar_serializer = DivarSerializer(divars, many=True)
        return JsonResponse(divar_serializer.data, safe=False)

    elif request.method == 'POST':
        divar_data = JSONParser().parse(request)
        divar_serializer = DivarSerializer(data=divar_data)
        if divar_serializer.is_valid():
            divar_serializer.save()
            return JsonResponse('Added successfully', safe=False)
        return JsonResponse({'error': 'Failed to add'}, status=400)

    elif request.method == 'PUT':
        divar_instance = get_object_or_404(Divar, pk=id)
        divar_data = JSONParser().parse(request)
        divar_serializer = DivarSerializer(divar_instance, data=divar_data)
        if divar_serializer.is_valid():
            divar_serializer.save()
            return JsonResponse('Updated successfully', safe=False)
        return JsonResponse({'error': 'Failed to update'}, status=400)
