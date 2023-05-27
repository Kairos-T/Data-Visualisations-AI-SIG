import plotly.graph_objects as go

# Data Set
labels = ['Category 1', 'Category 2', 'Category 3']
values = [30, 25, 45]

# Trace
trace = go.Pie(
    labels=labels,
    values=values,
    marker=dict(colors=['blue', 'green', 'red'])
)

# Create layout
layout = go.Layout(
    title='Pie Chart'
)

# Create figure
fig = go.Figure(data=[trace], layout=layout)

# Display the plot
fig.show()
