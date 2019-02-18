# bokeh serve --show "C:\Users\James\Documents\GitHub\test\bokeh.py"

from analyser import twitterquery, oandaquery
import datetime
from bokeh.layouts import row, column, gridplot
from bokeh.models import LinearAxis, ColumnDataSource, Range1d, Slider, Select
from bokeh.plotting import curdoc, figure
from bokeh.driving import count

source = ColumnDataSource(dict(
    oandatime=[],
    twittertime=[],
    PositiveTweets=[],
    NegativeTweets=[],
    priceask=[],
    pricebids=[]
))

p = figure(plot_height=300, x_axis_type="datetime", y_axis_location="right")


p.line(x='twittertime', y='PositiveTweets', alpha=0.8, line_width=3, color='green', source=source)
p.line(x='twittertime', y='NegativeTweets', alpha=0.8, line_width=3, color='red', source=source)

p2 = figure(plot_height=300, x_axis_type="datetime", y_axis_location="right")
p2.line(x='oandatime', y='priceask', alpha=0.8, line_width=3, color='green', source=source)
p2.line(x='oandatime', y='pricebids', alpha=0.8, line_width=3, color='red', source=source)

@ count()


def update(t):
    positiveteets, negativetweets, neutraltweets, twittertime = twitterquery.get_twitter_response()
    asks, bids, oandatime = oandaquery.stream()

    new_data = dict(
        twittertime=[twittertime],
        oandatime=[oandatime],
        PositiveTweets=[positiveteets],
        NegativeTweets=[negativetweets],
        priceask=[asks],
        pricebids=[bids]
    )

    source.stream(new_data)


curdoc().add_root(gridplot([[p],[p2]], plot_width=2000))
p.x_range = p2.x_range
curdoc().add_periodic_callback(update, 7000)
curdoc().title = "test"