import plotly.graph_objects as go

# Data Set
x = [1, 2, 3, 4, 5]
y = [3, 5, 2, 7, 4]

# Create a line trace
trace = go.Scatter(
    x=x,
    y=y,
    mode='lines',
    marker=dict(color='red')
)

# Create layout
layout = go.Layout(
    title='Line Plot',
    xaxis=dict(title='X'),
    yaxis=dict(title='Y')
)

# Create figure
fig = go.Figure(data=[trace], layout=layout)

# Display
fig.show()
