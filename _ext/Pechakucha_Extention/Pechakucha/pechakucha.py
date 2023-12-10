from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective
# Custom node classes
class PechakuchaSlide(nodes.Admonition, nodes.Element):
    pass

class PechakuchaSlideshow(nodes.General, nodes.Element):
    pass

# Directive for individual slides
class PechakuchaSlideDirective(SphinxDirective):
    has_content = True
    
    def run(self):
        text = '\n'.join(self.content)
        slide_node = PechakuchaSlide(text)
        return [slide_node]

# Directive for the slideshow
class PechakuchaSlideshowDirective(Directive):
    def run(self):
        return [PechakuchaSlideshow('')]

# Visitor functions for rendering (to be expanded)
def visit_pechakucha_slide_node(self, node):
    # HTML rendering for a slide
    pass

def depart_pechakucha_slide_node(self, node):
    # HTML rendering end for a slide
    pass

def visit_pechakucha_slideshow_node(self, node):
    # HTML rendering for the slideshow
     pass

def depart_pechakucha_slideshow_node(self, node):
    # HTML rendering end for the slideshow
    pass

# Setup function to register the extension with Sphinx
def setup(app):
    app.add_node(PechakuchaSlide,
                 html=(visit_pechakucha_slide_node, depart_pechakucha_slide_node))
    app.add_node(PechakuchaSlideshow,
                 html=(visit_pechakucha_slideshow_node, depart_pechakucha_slideshow_node))

    app.add_directive('pechakucha_slide', PechakuchaSlideDirective)
    app.add_directive('pechakucha_slideshow', PechakuchaSlideshowDirective)

    return {'version': '0.1', 'parallel_read_safe': True, 'parallel_write_safe': True}