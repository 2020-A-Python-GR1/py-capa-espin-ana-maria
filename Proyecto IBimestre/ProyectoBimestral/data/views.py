from django.shortcuts import render
from .models import Data, Purchase
import pandas as pd

# Create your views here.

def chart_select_view(request):
    product_df = pd.DataFrame(Data.objects.all().values())
    Purchase_df = pd.DataFrame(Purchase.objects.all().values())
    product_df['data_id'] = product_df['id']
    df= pd.merge(Purchase_df,product_df, on='data_id').drop(['id_y', 'date_y'], axis=1).rename({'id_x' : 'id', 'date_x' : 'date'}, axis=1)
    context = {
        'products' : product_df.to_html(), 
        'purchase' : Purchase_df.to_html(),
        'df': df.to_html(),
    }
    
    return render(request, 'products/main.html',context)

    
    

