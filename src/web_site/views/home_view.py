from flask import render_template


class HomeView:
    def __init__(self):
        pass

    def get(self):
        return render_template(template_name_or_list="home/index.jinja2"), 200
