import plotly.graph_objects as go

# Data Set
x = ['A', 'B', 'C', 'D']
y = [20, 14, 23, 18]

# Bar trace
trace = go.Bar(
    x=x,
    y=y,
    marker=dict(color='black')
)

# Create layout
layout = go.Layout(
    title='Bar Graph',
    xaxis=dict(title='Categories'),
    yaxis=dict(title='Values')
)

# Create figure
fig = go.Figure(data=[trace], layout=layout)

# Display plot
fig.show()
