from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util.docutils import SphinxDirective

class SlideshowDirective(SphinxDirective):
    has_content = True

    def run(self):
        container = nodes.container('', classes=['slideshow'])
        self.set_source_info(container)

        for image_path in self.content:
            image_node = nodes.image(uri=image_path)
            container += nodes.figure('', image_node)

        return [container]

def setup(app):
    app.add_directive("slideshow", SlideshowDirective)
    app.add_css_file('slideshow.css')
    app.add_js_file('slideshow.js')

    return {'version': '0.1', 'parallel_read_safe': True, 'parallel_write_safe': True}
