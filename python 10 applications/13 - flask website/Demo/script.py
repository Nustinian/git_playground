from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/plot')
@app.route('/plot/')
def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.models.annotations import Title
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN

    start = datetime.datetime(2019, 8, 16)
    end = datetime.datetime(2020, 1, 16)
    df = data.DataReader(name = "AAPL", data_source = "yahoo", start = start, end = end )

    def increase_or_decrease(close, open):
        if close > open:
            value = "Increase"
        elif close < open:
            value = "Decrease"
        else:
            value = "Equal"
        return value

    df["Status"] = [increase_or_decrease(close, open) for close, open in zip(df.Close, df.Open)]
    df["Middle"] = (df.Open + df.Close) / 2
    df["Height"] = abs(df.Close - df.Open)

    p = figure(x_axis_type = 'datetime', width = 1000, height = 300, sizing_mode = 'scale_width')
    title = Title()
    title.text = "Candlestick Chart"
    p.title = title
    p.grid.grid_line_alpha = 0.3

    hours_12 = 12 * 60 * 60 * 1000

    p.segment(df.index, df.Low, df.index, df.High, color = "Black")

    p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], hours_12, 
           df.Height[df.Status == "Increase"], fill_color = "#27AF39", line_color = "black")
    p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"], hours_12,
           df.Height[df.Status == "Decrease"], fill_color = "#DB1D1D", line_color = "black")

    script1, div1 = components(p)
    cdn_js = CDN.js_files
    return render_template("plot.html", script1=script1, div1=div1, cdn_js=cdn_js[0])
    
if __name__ == "__main__":
    app.run(debug=True)