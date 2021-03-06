'''
Created on 2013-12-23

@author: Adam Gignac
'''

from gi.repository import Gtk
from embedcontextpane import EmbedContextPane

class WikiContextPane(Gtk.HBox, EmbedContextPane):
    def __init__(self):
        super(WikiContextPane, self).__init__()
        self.add(Gtk.Label(label="Subject: "))
        self.entry = Gtk.Entry()
        self.add(self.entry)
        self.show_all()
    
    def getHtml(self):
        text = self.entry.get_text()
        url =  "http://en.wikipedia.org/wiki/%s" % (text.replace(" ", "_"))
        return '<div class="collapsible" onClick="toggleDiv(this)"><p>Wikipedia: %s</p><iframe src="%s"></iframe></div><br/>' % (text, url)

def register():
    return ("Wikipedia", WikiContextPane())
