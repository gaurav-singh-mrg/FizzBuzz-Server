from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Count
from .models import RequestStat

# schema_view = get_swagger_view(title='fizz_buzz')


@api_view(['GET'])
def fizz_buzz(request, int1, int2, limit, str1, str2):
    """
        Fizz-Buzz endpoint Input Field Description.\n
        :param int1: Integer, multiples of which will be replaced with str1.\n
        :param int2: Integer, multiples of which will be replaced with str2.\n
        :param limit: Integer, defines the range of numbers (from 1 to limit) for the Fizz-Buzz logic.\n
        :param str1: String, the replacement for multiples of int1.\n
        :param str2: String, the replacement for multiples of int2.\n
        :return: List of strings representing the Fizz-Buzz output.\n
    """
    result = []

    for num in range(1, limit + 1):
        fizz_buzz_str = ''
        if num % int1 == 0:
            fizz_buzz_str += str1
        if num % int2 == 0:
            fizz_buzz_str += str2

        result.append(fizz_buzz_str or str(num))

    # Save the request statistics
    RequestStat.objects.create(int1=int1, int2=int2, limit=limit, str1=str1, str2=str2)

    return Response(result)


@api_view(['GET'])
def statistics(request):
    """
        Statistics endpoint.\n
        This endpoint does not require any parameters.\n
        :return: JSON response containing statistics of the most used request.\n
    """
    most_used_request = RequestStat.objects.values('int1', 'int2', 'limit', 'str1', 'str2').annotate(
        count=Count('id')).order_by('-count').first()

    if most_used_request:
        response_data = {
            'int1': most_used_request['int1'],
            'int2': most_used_request['int2'],
            'limit': most_used_request['limit'],
            'str1': most_used_request['str1'],
            'str2': most_used_request['str2'],
            'count': most_used_request['count'],
        }
        # return Response(response_data)
        return JsonResponse(response_data)
    else:
        return JsonResponse({'message': 'No statistics available'})
