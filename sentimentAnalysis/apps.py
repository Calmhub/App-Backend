from django.apps import AppConfig
from django.conf import settings


class SentimentanalysisConfig(AppConfig):
    # path = os.path.join(settings.BASE_DIR, 'sentimentAnalysis','models', 'Mental.p')

    # with open(path,'rb') as pickled:
    #     data = pickle.load(pickled)
    
    # model = data['model']
    # vectorizer = data['vectorizer']

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sentimentAnalysis'
