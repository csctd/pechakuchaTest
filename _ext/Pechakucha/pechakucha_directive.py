from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from docutils.parsers.rst import directives

class PechaKuchaDirective(SphinxDirective):
    has_content = True
    option_spec = {
        'transition_time': directives.positive_int,
    }

    def run(self):
        transition_time = self.options.get('transition_time', 3)  # Default to 3 seconds

        container = nodes.container('', classes=['pechakucha-slideshow'])
        container['data-transition-time'] = str(transition_time)

        self.set_source_info(container)

        for image_path in self.content:
            image_node = nodes.image(uri=image_path)
            figure_node = nodes.figure('', image_node)
            container += figure_node

        return [container]
    
def setup(app):
    app.add_directive("pechakucha", PechaKuchaDirective)
    app.add_css_file('pechakucha/static/slideshow.css')
    app.add_js_file('pechakucha/static/slideshow.js')

    return {'version': '0.1', 'parallel_read_safe': True, 'parallel_write_safe': True}
