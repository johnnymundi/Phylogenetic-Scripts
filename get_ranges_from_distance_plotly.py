import plotly.graph_objects as go

# Read in distances from file
with open('Xborealis_distance.txt') as f:
    distances = [int(line.strip()) for line in f]

# Define range size and maximum distance
range_size = 1000
max_distance = 100000

# Create range boundaries using the range function
ranges = list(range(0, max_distance, range_size))

# Count the number of distances that fall within each range using a list comprehension
counts = [len([d for d in distances if r <= d < r+range_size]) for r in ranges]

# Define x-axis tick values and labels
x_ticks = [i*20000 for i in range(1, int(max_distance/20000)+1)]
x_tick_labels = ['{}'.format(i*20) for i in range(1, int(max_distance/20000)+1)]

# Create Plotly figure
fig = go.Figure()

# Add histogram trace
fig.add_trace(go.Histogram(x=distances, xbins=dict(start=0, end=max_distance, size=range_size),
                            marker_color='black'))

# Update x-axis properties
fig.update_xaxes(title_text='Distance (kilobases)', tickvals=x_ticks, ticktext=x_tick_labels)

# Update y-axis properties
fig.update_yaxes(title_text='Frequency')

# Show plot
fig.show()
