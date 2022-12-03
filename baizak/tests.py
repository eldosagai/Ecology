from django.test import TestCase
from models import Article
import pandas as pd
print(pd.DataFrame(Article.objects.all().values()))

# Create your tests here.
