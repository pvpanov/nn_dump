import dash

app = dash.Dash()

app.layout = dash.html.Div(
    [
        dash.html.H1("Dash App with Two Tabs"),
        dash.dcc.Tabs(
            id="tabs",
            value="tab-1",
            children=[
                dash.dcc.Tab(label="Tab One", value="tab-1"),
                dash.dcc.Tab(label="Tab Two", value="tab-2"),
            ],
        ),
        dash.html.Div(id="tabs-content"),
    ]
)


@app.callback(dash.Output("tabs-content", "children"), [dash.Input("tabs", "value")])
def render_content(tab):
    if tab == "tab-1":
        return dash.html.Div([dash.html.H3("Tab One Content")])
    elif tab == "tab-2":
        return dash.html.Div([dash.html.H3("Tab Two Content")])


if __name__ == "__main__":
    app.run_server(debug=True)
