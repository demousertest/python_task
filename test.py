import pandas as pd
# import plotly.graph_objects as go
import plotly.express as px


df = pd.read_excel(r'C:\Users\Hemant Mahawer-3348\Desktop\all task\python_task\heatmap_data.xlsx')
# print(df)
fig = px.treemap(df, path=['Area'], values='Existing Team Members Proficient with this area',
                 color='Average Team Expertise (1-5)', 
                 color_discrete_map={'Dark Green': 'rgb(88, 175, 78)',
                                      'One Level Below Dark green': 'rgb(95, 175, 78)',
                                      'One level Above Light green': 'rgb(191, 225, 182)',
                                      'Two Level Above Light green' : "rgb(180, 255, 153)",
                                      'White':'rgb(255, 255, 255)',
                                      'Light Green': "rgb(144, 238, 144)",
                                      'Two Level Below Dark green': 'rgb(134, 230, 132)'})
fig.show()