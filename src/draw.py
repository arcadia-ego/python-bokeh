import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, Circle, ColumnDataSource, Range1d, LabelSet, Label
from bokeh.palettes import Spectral8
from graph import *

WIDTH = 640
HEIGHT = 480
CIRCLE_SIZE = 30

graph_data = Graph()
graph_data.debug_create_test_data()
graph_data.get_connected_components()

print("graph vertexes",graph_data.vertexes)
N = len(graph_data.vertexes)
print("N", [0]*N)

node_indices = list(range(N))
print("node indices", node_indices)

color_list = []
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)

plot = figure(title='Graph Layout Demonstration', x_range=(0,WIDTH), y_range=(0, HEIGHT),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Circle(size=30, fill_color="color")

# HINT: DRAWING EDGES FORM START TO END
start_indexes = []
end_indexes = []
for start_index, vertex in enumerate(graph_data.vertexes):
    for e in vertex.edges:
        start_indexes.append(start_index)
        end_indexes.append(graph_data.vertexes.index(e.destination))

graph.edge_renderer.data_source.data = dict(
    start=start_indexes, # list has to do with starting points: goes from [0,0,0] -> [0,1,2]; want [x,x,x] -> [y,y,y]
    end=end_indexes) #list that has to do with ending points

### start of layout code
x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)
## LABEL


# create a new dict to use as a data source with three lists ordered in the same way as vertexes
value = [v.value for v in graph_data.vertexes] #TODO possible optimization: run through this loop three times

label_source = ColumnDataSource(data=dict(x=x, y=y, v=value))


labels = LabelSet(x='x', y='y', text='v', level='overlay',
                  source=label_source, render_mode='canvas', text_align="center")

plot.add_layout(labels)
##/LABEL

plot.renderers.append(graph)

output_file('graph.html')
show(plot)
