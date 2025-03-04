from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .grep_code.agrep import grep_func
from .grep_code.ocr import img_query

# Create your views here.
@api_view(['POST'])
def run_upload(request):
    print(f'REQUEST RECEIVED {request}')
    if 'photo' in request.FILES:
        image = request.FILES['photo']
        try:
            extracted_text = img_query(image)
            return Response({'extracted_text': extracted_text}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({'error': 'No photo found in request'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def run_grep(request):
    
    w = request.query_params.get('string', None)
    r = request.query_params.get('regex', None)
    
    if not w: w = ""
    if not r: r = ""

    # if w is None or r is None: return Response({'error': 'Missing query parameters'}, status=status.HTTP_400_BAD_REQUEST)

    # Call the grep function with the provided parameters
    accept, nfa, path = grep_func(w, r)
    
    # Result of grep
    result = {
        'status': accept,
        'nfa': nfa,
        'path': path,
    }
    
    return Response(result, status=status.HTTP_200_OK)
    
    
    
    # # request include a dictionary in its .data, which we specify in the action to hold 'string' and 'regex' key value pairs
    # print(request)
    # print(request.data)
    # w, r = request.data['string'], request.data['regex']
    # # grep function from python script
    # accept, nfa, path = grep_func(w, r)
    
    # # result of grep
    # result = {
    #     'status': accept,
    #     'nfa': nfa,
    #     'path': path,
    # }
    
    # return Response(result, status=status.HTTP_200_OK)
