import pandas as pd
import plotly.graph_objects as go


data = pd.read_excel('heatmap_data.xlsx')

data_list = data.values.tolist()

# Create lists for treemap
labels = [f"{row[0]} ({row[1]})" for row in data_list]
parents = ["" for _ in data_list]
values = [row[1] for row in data_list]


color_mapping = {
    (30, 25): 'rgb(80, 173, 71)',
    (24, 20): 'rgb(100, 173, 71)',
    (19, 15): 'rgb(169, 208, 142)',
    (14, 10): 'rgb(198, 224, 180)',
    (9, 5): 'rgb(226, 239, 218)',
    (4, 0): 'rgb(236, 239, 240)',
}

colors = []
for value in values:
    for key, color in color_mapping.items():
        if key[0] >= value >= key[1]:
            colors.append(color)
            break


custom_data = [[f"Area: {row[0]}", f"Value: {row[1]}", f"Color: {row[2]}"] for row in data_list]

# Create treemap trace
trace = go.Treemap(
    labels=labels,
    parents=parents,
    values=values,
    marker=dict(colors=colors),
    customdata=custom_data,  # Add custom data
    hovertemplate="<b>%{customdata[0]}</b><br>%{customdata[1]}<br>%{customdata[2]}<extra></extra>",
)


layout = go.Layout(
    title="Treemap Visualization",
)


fig = go.Figure(data=[trace], layout=layout)
fig.show()
