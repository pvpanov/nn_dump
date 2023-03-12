import dash
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output


app = dash.Dash()

app.layout = html.Div(
    [
        html.H1("Dash App with Two Tabs"),
        dcc.Tabs(
            id="tabs",
            value="tab-1",
            children=[
                dcc.Tab(label="Tab One", value="tab-1"),
                dcc.Tab(label="Tab Two", value="tab-2"),
            ],
        ),
        html.Div(id="tabs-content"),
    ]
)


@app.callback(Output("tabs-content", "children"), [Input("tabs", "value")])
def render_content(tab):
    if tab == "tab-1":
        return html.Div([html.H3("Tab One Content")])
    elif tab == "tab-2":
        return html.Div([html.H3("Tab Two Content")])


if __name__ == "__main__":
    app.run_server(debug=True)
