from django.shortcuts import render

from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN


def simple_graph(request):
    plot = figure()
    plot.circle([1, 2], [3, 4])

    plot.circle()

    script, div = components(plot, CDN)

    return render(request, 'dashboard/dashboard.html',
                  {'dashboard_script': script, 'plot_div': div})
