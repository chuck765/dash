
import dash  
import dash_core_components as dcc 
import dash_html_components as html  

app = dash.Dash(__name__)

app.layout = html.Div(
   children =[
    html.H1('Hello Chuck app',),
    dcc.Graph(
        id = "first-graph",
        figure = {
        'data': [
            {'x': [1,2,3,4],
            'y':[3,2,4,6],
            'type': 'bar',
            'name': '東京'},
            {'x':[1,2,3,4],
            'y':[2,4,3,2],
            'type': 'bar',
            'name': '大阪'}
        ],
        'layout': {
            'title': 'グラフ1　東京　対　大阪'
        }
        }
    )
])

# 実行用③
if __name__=='__main__':
    app.run_server(debug=True)