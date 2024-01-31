from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from docutils.parsers.rst import directives

class PechaKuchaDirective(SphinxDirective):
    has_content = True
    option_spec = {
        'transition_time': directives.positive_int,
    }

    def run(self):
        transition_time = self.options.get('transition_time', 3000)

        container = nodes.container('', classes=['pechakucha-slideshow'])
        container['data-transition-time'] = str(transition_time)

        self.set_source_info(container)

        for image_path in self.content:
            image_node = nodes.image(uri=image_path, classes=['pechakucha-slide'])
            figure_node = nodes.figure('', image_node, classes=['align-default'])
            container += figure_node

        # Add navigation buttons
        nav_container = nodes.container('', classes=['pechakucha-controls'])
        prev_button = nodes.raw('', '<button id="prev-slide">Previous</button>', format='html')
        next_button = nodes.raw('', '<button id="next-slide">Next</button>', format='html')
        nav_container.extend([prev_button, next_button])
        container += nav_container

        # Add progress indicator container
        progress_container = nodes.container('', classes=['pechakucha-progress'])
        container += progress_container

        script_node = nodes.raw('', "<script src='_static/pechakucha.js'></script>", format='html')
        container += script_node

        return [container]


def setup(app):
    app.add_directive("pechakucha", PechaKuchaDirective)
    app.add_css_file('_static/pechakucha.css')
    app.add_js_file('_static/pechakucha.js')

    return {'version': '0.1', 'parallel_read_safe': True, 'parallel_write_safe': True}
