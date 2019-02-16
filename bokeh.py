# bokeh serve --show "C:\Users\James\Documents\GitHub\test\bokeh.py"

from analyser import twitterquery, oandaquery
import datetime
from bokeh.layouts import row, column, gridplot
from bokeh.models import ColumnDataSource, Slider, Select
from bokeh.plotting import curdoc, figure
from bokeh.driving import count

source = ColumnDataSource(dict(
    time=[],
    PositiveTweets=[],
    NegativeTweets=[],
    priceask=[],
    pricebids=[]
))

p = figure(plot_height=500, tools="xpan,xwheel_zoom,xbox_zoom,reset", x_axis_type="datetime", y_axis_location="right")
p.x_range.follow = "end"
p.x_range.follow_interval = 100
p.x_range.range_padding = 0

p.line(x='time', y='PositiveTweets', alpha=0.8, line_width=3, color='green', source=source)
p.line(x='time', y='NegativeTweets', alpha=0.8, line_width=3, color='red', source=source)

p2 = figure(plot_height=500, tools="xpan,xwheel_zoom,xbox_zoom,reset", x_axis_type="datetime", y_axis_location="right")
p2.line(x='time', y='priceask', alpha=0.8, line_width=3, color='green', source=source)
p2.line(x='time', y='pricebids', alpha=0.8, line_width=3, color='red', source=source)



@count()
def update(t):
    positiveteets, negativetweets, neutraltweets, testtime = twitterquery.get_twitter_response(t)
    asks, bids = oandaquery.stream(t)

    new_data = dict(
        time=[testtime],
        PositiveTweets=[positiveteets],
        NegativeTweets=[negativetweets],
        priceask=[asks],
        pricebids=[bids]
    )

    source.stream(new_data, 300)


curdoc().add_root(gridplot([[p],[p2]], plot_width=2000))
curdoc().add_periodic_callback(update, 5000)
curdoc().title = "brexit"
