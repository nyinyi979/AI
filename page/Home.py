from dash import html
from page.home.Home import Home


layout = html.Div(
    [Home()],
    className="relative",
)
