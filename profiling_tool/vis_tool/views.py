import pandas as pd
from django.shortcuts import HttpResponse, Http404
from rest_pandas import PandasSimpleView, PandasView
from rest_pandas.renderers import PandasHTMLRenderer, PandasCSVRenderer

# Create your views here.


class TimeSeriesView(PandasSimpleView):
    def get_data(self, request, *args, **kwargs):
        dataframe = request.GET.get("dataframe", None)
        if dataframe is not None and dataframe.lower() in {"cas" "acc", "veh"}:
            filepath = 'vis_tool/data/{}.csv'.format(dataframe.capitalize())
        else:
            filepath = 'vis_tool/data/Cas.csv'
        df = pd.read_csv(filepath, dtype={'Accident_Index': str})
        columns = request.GET.get("columns", None)
        if columns is not None and all([x in df.columns for x in columns.split(",")]):
            result_df = df[columns.split(",")]
        else:
            result_df = df
        return result_df

    renderer_classes = [PandasHTMLRenderer]
    template_name = 'vis_tool/index.html'
