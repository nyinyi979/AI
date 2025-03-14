import dash
from dash import Dash, html, Output, Input, ctx
from components.Button import Button
from page.DataDialog import DataDialog
from utils.CacheManager import background_callback_manager

app = Dash(
    __name__, use_pages=True, background_callback_manager=background_callback_manager
)

app.layout = html.Div(
    [
        DataDialog(),
        html.Div(
            [
                Button(
                    children="Home",
                    variant="primary_ghost",
                    size="sm",
                    asLink=True,
                    href="/",
                ),
                Button(
                    children="Analysis",
                    variant="primary_ghost",
                    size="sm",
                    asLink=True,
                    href="/analysis",
                ),
                Button(
                    children="Epsilon",
                    variant="primary_ghost",
                    size="sm",
                    asLink=True,
                    href="/epsilon",
                ),
                Button(
                    children=["Login", html.Img(src="/assets/images/icons/login.svg")],
                    variant="primary",
                    size="sm",
                    asLink=True,
                    href="/login",
                    className="flex items-center gap-2.5",
                ),
                Button(
                    children="Signup",
                    variant="primary_ghost",
                    size="sm",
                    asLink=True,
                    href="/signup",
                ),
            ],
            style={"boxShadow": "0 0 25px 0 hsla(180, 30%, 82%, 0.50)"},
            className="w-full sticky top-0 left-0 flex gap-[30px] justify-end items-center px-20 py-3 backdrop-blur-sm bg-[#EEFFFF]/80 z-[100]",
        ),
        dash.page_container,
    ],
    className="relative",
)

if __name__ == "__main__":
    app.run(debug=True)
