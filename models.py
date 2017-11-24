from google.appengine.ext import ndb

class Gost(ndb.Model):
    ime = ndb.StringProperty()
    priimek = ndb.StringProperty()
    email = ndb.StringProperty()
    sporocilo = ndb.TextProperty()
    datum = ndb.DateProperty(auto_now_add=True)
