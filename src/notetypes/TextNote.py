'''
Created on 2013-10-19

@author: Adam Gignac
'''
from gi.repository import Gtk, WebKit
from AbstractNote import AbstractNote

class TextNote(Gtk.ScrolledWindow, AbstractNote):
    '''
    A text-based note.
    '''


    def __init__(self, sourceFile=None):
        '''
        Constructor. If sourceFile is specified, the contents of
        sourceFile will be contained in the page.
        '''
        super(TextNote, self).__init__(None, None)
        self.webview = WebKit.WebView()
        #Populate the page with dummy text as proof of concept
        content = """
<body>
    <b>This is bold</b>
    <i>This is italicized</i>
    <u>This is underlined</u>
    <ul>
        <li>This is an unordered list</li>
        <li>With multiple items</li>
    </ul>
    <ol>
        <li>This is an ordered list</li>
        <li>With multiple items</li>
    </ol>
    <p>Wikipedia page embedded:</p>
    <iframe src="https://en.wikipedia.org/wiki/HTML_element#Frames" style="width:80%"></iframe>
</body>
""" 
        self.webview.load_html_string(content, "file:///")
        self.add(self.webview)
        self.webview.set_editable(True)
        self.show_all()

    def saveContents(self):
        '''
        Extracts the contents of the page and writes them to a file.
        '''
        raise NotImplementedError()

    def getContextToolbarItems(self):
        '''
        Returns a list of toolbar items that are specific to the note
        type (i.e. text formatting for text notes, drawing tools for
        a diagram, etc)
        '''
        bold = Gtk.ToolButton(Gtk.STOCK_BOLD)
        bold.connect('clicked', self.onBoldClicked)
        italic = Gtk.ToolButton(Gtk.STOCK_ITALIC)
        italic.connect('clicked', self.onItalicClicked)
        underline = Gtk.ToolButton(Gtk.STOCK_UNDERLINE)
        underline.connect('clicked', self.onUnderlineClicked)
        embed = Gtk.ToolButton(Gtk.STOCK_NEW)
        embed.connect('clicked', self.onEmbedClicked)
        indent = Gtk.ToolButton(Gtk.STOCK_INDENT)
        indent.connect('clicked', self.onIndentClicked)
        unindent = Gtk.ToolButton(Gtk.STOCK_UNINDENT)
        unindent.connect('clicked', self.onUnindentClicked)
        unorderedList = Gtk.ToolButton()
        unorderedList.connect('clicked', self.onUnorderedListClicked)
        orderedList = Gtk.ToolButton()
        orderedList.connect('clicked', self.onOrderedListClicked)
        leftJustify = Gtk.ToolButton(Gtk.STOCK_JUSTIFY_LEFT)
        leftJustify.connect('clicked', self.onLeftJustifyClicked)
        centerJustify = Gtk.ToolButton(Gtk.STOCK_JUSTIFY_CENTER)
        centerJustify.connect('clicked', self.onCenterJustifyClicked)
        rightJustify = Gtk.ToolButton(Gtk.STOCK_JUSTIFY_RIGHT)
        rightJustify.connect('clicked', self.onRightJustifyClicked)
        undo = Gtk.ToolButton(Gtk.STOCK_UNDO)
        undo.connect('clicked', self.onUndoClicked)
        redo = Gtk.ToolButton(Gtk.STOCK_REDO)
        redo.connect('clicked', self.onRedoClicked)
        
        return [bold, italic, underline, embed, indent, unindent, 
                unorderedList, orderedList, leftJustify, centerJustify,
                rightJustify, undo, redo]
    
    def onBoldClicked(self, button):
        self.webview.execute_script("document.execCommand('bold', false, false);")
    
    def onItalicClicked(self, button):
        self.webview.execute_script("document.execCommand('italic', false, false);")
    
    def onUnderlineClicked(self, button):
        self.webview.execute_script("document.execCommand('underline', false, false);")
    
    def onEmbedClicked(self, button):
        #TODO: Present popup asking about what to embed
        html = '<iframe src="http://en.wikipedia.org/wiki/JavaScript" style="width:80%; height:200px;"></iframe>'
        self.webview.execute_script("document.execCommand('insertHTML', false, '%s');" % (html,))
    
    def onIndentClicked(self, button):
        self.webview.execute_script("document.execCommand('indent', false, false);")
    
    def onUnindentClicked(self, button):
        self.webview.execute_script("document.execCommand('outdent', false, false);")
    
    def onUnorderedListClicked(self, button):
        self.webview.execute_script("document.execCommand('insertUnorderedList', false, false);")
    
    def onOrderedListClicked(self, button):
        self.webview.execute_script("document.execCommand('insertOrderedList', false, false);")
    
    def onLeftJustifyClicked(self, button):
        self.webview.execute_script("document.execCommand('justifyleft', false, false);")
    
    def onCenterJustifyClicked(self, button):
        self.webview.execute_script("document.execCommand('justifycenter', false, false);")
    
    def onRightJustifyClicked(self, button):
        self.webview.execute_script("document.execCommand('justifyright', false, false);")
    
    def onUndoClicked(self, button):
        self.webview.execute_script("document.execCommand('undo');")
    
    def onRedoClicked(self, button):
        self.webview.execute_script("document.execCommand('redo');")
