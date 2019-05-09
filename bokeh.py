# bokeh serve --show "C:\Users\James\Documents\GitHub\test\bokeh.py"

from oanda import oandaquery
from bokeh.layouts import row, column, gridplot
from bokeh.models import LinearAxis, ColumnDataSource, Range1d, Slider, Select
from bokeh.plotting import curdoc, figure
from bokeh.driving import count

source = ColumnDataSource(dict(
    oandatime=[],
    mid=[],
    priceask=[],
    pricebids=[]
))

p = figure(plot_height=900, x_axis_type="datetime", y_axis_location="right")

p.line(x='oandatime', y='priceask', alpha=0.8, line_width=3, color='black', source=source)
p.line(x='oandatime', y='pricebids', alpha=0.8, line_width=3, color='black', source=source)
p.line(x='oandatime', y='mid', alpha=0.8, line_width=3, color='blue', source=source)


@count()


def update(t):
    asks, bids, oandatime = oandaquery.get_oanda_response(t)
    mid = (asks + bids) / 2
    new_data = dict(
        mid=[mid],
        oandatime=[oandatime],
        priceask=[asks],
        pricebids=[bids]
    )

    source.stream(new_data)


curdoc().add_root(gridplot([[p]], plot_width=2000))
curdoc().add_periodic_callback(update, 1)
curdoc().title = "test"
