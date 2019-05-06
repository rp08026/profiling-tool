import pandas as pd
from django.shortcuts import HttpResponse, Http404
from rest_pandas import PandasSimpleView, PandasView
from rest_pandas.renderers import PandasHTMLRenderer, PandasCSVRenderer

# Create your views here.


class TimeSeriesView(PandasSimpleView):
    def get_data(self, request, *args, **kwargs):
        dataframe = request.GET.get("dataframe", None)
        if dataframe is not None and dataframe.lower() in {"cas" "acc", "veh"}:
            data = 'vis_tool/data/{}.csv'.format(dataframe.capitalize())
        else:
            data = 'vis_tool/data/Cas.csv'
        return pd.read_csv(data, dtype={'Accident_Index': str})

    renderer_classes = [PandasHTMLRenderer]
    template_name = 'vis_tool/index.html'
