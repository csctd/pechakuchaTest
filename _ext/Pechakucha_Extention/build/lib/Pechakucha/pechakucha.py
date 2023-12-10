from docutils import nodes
from docutils.parsers.rst import Directive


class PechakuchaDirective(Directive):
    has_content = True # Indicates that this directive expects content
    def run(self):
         # Create a node to be added to the document
        paragraph_node = nodes.paragraph(text='Test Text!')
        return [paragraph_node]

    def setup(app):
        app.add_directive("pechakucha", PechakuchaDirective)