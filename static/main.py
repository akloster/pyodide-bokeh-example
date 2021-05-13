import js
import bokeh
from bokeh.plotting import figure
import numpy as np
x = np.linspace(-6, 6, 100)
y = np.cos(x)
p = figure(width=500, height=500)
p.circle(x, y, size=7, color="firebrick", alpha=0.5)
script, div = bokeh.embed.components(p)
container = js.document.getElementById("container")
container.innerHTML=div
tmp = js.document.createElement("div")
tmp.innerHTML = script
js.eval(tmp.innerText)