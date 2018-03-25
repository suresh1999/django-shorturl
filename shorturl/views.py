from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import Short, LongUrlException
# Create your views here.

#Class based view used to generate a short-url for an long-url
class GenerateURL(APIView):
    def post(self, request):
        if request.data.get('long_url'):
            url = request.data.get('long_url')
            try:
                s_url = None
                if request.GET['len']:
                    s_url = Short(url, int(request.GET['len']))
                else:
                    s_url = Short(url)
                out = s_url.generate()
            except LongUrlException:
                return Response({"Invalid":"Long url already exists"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            return Response({"short-url":out}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"long_url attribute not found in the json"}, status=status.HTTP_400_BAD_REQUEST)


#Class Based View used to retrive the long url for an given short url
class CheckURL(APIView):
    def post(self, request):
        if request.data.get('short_url'):
            url = request.data.get('short_url')
            try:
                s_url = Short.get_longurl(url)
            except LongUrlException as e:
                return Response({"Invalid":e.msg}, status=status.HTTP_406_NOT_ACCEPTABLE)
            return Response({"long-url":s_url}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"short_url attribute not found in the json"}, status=status.HTTP_400_BAD_REQUEST)

class GenerateURLS(APIView):
    def post(self, request, *args, **kwargs):
        result = []
        urls = request.data.get('short_urls')
        if urls:
            for url in urls:
                try:
                    u = Short(url)
                    result.append(u.generate())
                except LongUrlException:
                    result.append("This url already exists")
        return Response({"long_url":urls,"short_urls":result}, status=status.HTTP_200_OK)


class CheckURLS(APIView):
    def post(self, request):
        result = []
        urls = request.data.get('long_urls')
        if urls:
            for url in urls:
                try:
                    result.append(Short.get_longurl(url))
                except LongUrlException:
                    result.append("No match found")
        return Response({"long_url": urls, "short_urls": result}, status=status.HTTP_200_OK)

