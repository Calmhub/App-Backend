from django.shortcuts import render

from .apps import SentimentanalysisConfig
from django.http import JsonResponse
from rest_framework.views import APIView
from .sentiment_analysis_code import sentiment_analysis_code
from .models import SentimentRecord
from openai import OpenAI
import os
# Create your views here.


# class call_model(APIView):
#     def get(self,request):
#         if request.method == 'GET':
#             text = request.GET.get('text')

#             vector = SentimentanalysisConfig.vectorizer.transform([text])

#             prediction = SentimentanalysisConfig.model.predict(vector)[0]

#             response = {'text_sentiment' : prediction}
#             return JsonResponse(response)
        
class senti_analyse(APIView):
    def get(self,request):
        if request.method == 'GET':
            text = request.GET.get('text')

            model = sentiment_analysis_code()
            result = model.get_tweet_sentiment(text)

            response = {'text_sentiment' : result}

            record = SentimentRecord.objects.create(
                prediction = result
            )

            record.save()
            
            return JsonResponse(response, status = 200)

class chatbot(APIView):
    def get(self,request):
        client = OpenAI(
            api_key= "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"
        )
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a friendly psychiatrist"},{
                "role": "user", "content":request.GET.get('text')
            }],
            )
        output = stream.choices[0].message.content
        response = {'output':output}
        return JsonResponse(response,status = 200)
class getsentirecord(APIView):
    def get(self,request):
        negative_count = SentimentRecord.objects.filter(prediction="Negative").count()
        neutral_count = SentimentRecord.objects.filter(prediction="Neutral").count()
        positive_count = SentimentRecord.objects.filter(prediction="Positive").count()

        response = {'NegativeCount' : negative_count, 'NeutralCount': neutral_count, 'PositiveCount': positive_count}
        return JsonResponse(response,status = 200)



