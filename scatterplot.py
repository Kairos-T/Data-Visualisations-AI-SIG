import plotly.express as px

# Data Set
x = [1, 2, 3, 4, 5]
y = [3, 5, 2, 7, 4]

# Scatter Plot
fig = px.scatter(x=x, y=y)

# Adding title and axis layout
fig.update_layout(
    title="Scatter Plot",
    xaxis_title="X",
    yaxis_title="Y"
)

# Displaying the plot
fig.show()
