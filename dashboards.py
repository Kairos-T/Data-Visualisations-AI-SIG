import plotly.graph_objects as go
import plotly.subplots as sp

# Data Set
x = [1, 2, 3, 4, 5]
y1 = [3, 5, 2, 7, 4]
y2 = [6, 2, 4, 8, 5]

# Fig1
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='Line Plot'))

# Fig2
fig2 = go.Figure()
fig2.add_trace(go.Bar(x=x, y=y2, name='Bar Chart'))

# subplot dashboard
fig = sp.make_subplots(rows=1, cols=2, subplot_titles=('Line Plot', 'Bar Chart'))
fig.add_trace(fig1.data[0], row=1, col=1)
fig.add_trace(fig2.data[0], row=1, col=2)

fig.update_layout(height=400, width=800, title_text='Dashboard')

# Display
fig.show()
