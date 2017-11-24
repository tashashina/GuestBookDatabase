#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Gost


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("Filton.html")
    def post(self):
        ime = self.request.get("ime")
        priimek = self.request.get("priimek")
        email = self.request.get("email")
        sporocilo = self.request.get("sporocilo")

        if ime=="" and priimek=="":
            ime = "neznanec"
            priimek = ""

        gost = Gost(ime=ime,priimek=priimek,email=email,sporocilo=sporocilo)
        gost.put()
        return self.write(gost)

class SeznamGostovHandler(BaseHandler):
    def get(self):
        seznam = Gost.query().fetch()
        params = {"seznam": seznam}
        return self.render_template("seznam_gostov.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/seznam-gostov', SeznamGostovHandler),

], debug=True)