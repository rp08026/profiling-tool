import pandas as pd
from django.shortcuts import HttpResponse
from rest_pandas import PandasSimpleView, PandasView
from rest_pandas.renderers import PandasHTMLRenderer, PandasCSVRenderer

# Create your views here.


class TimeSeriesView(PandasSimpleView):
    def get_data(self, request, *args, **kwargs):
        return pd.read_csv('vis_tool/data/Cas.csv', dtype={'Accident_Index': str})

    renderer_classes = [PandasHTMLRenderer]
    template_name = 'vis_tool/index.html'
