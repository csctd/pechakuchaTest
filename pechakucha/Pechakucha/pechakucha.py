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
        slide_node = PechakuchaSlide()
        self.state.nested_parse(self.content, self.content_offset, slide_node)
        return [slide_node]

# Directive for the slideshow
class PechakuchaSlideshowDirective(Directive):
    has_content = True

    def run(self):
        slideshow_node = PechakuchaSlideshow()
        self.state.nested_parse(self.content, self.content_offset, slideshow_node)
        return [slideshow_node]

# Visitor functions for rendering
def visit_pechakucha_slide_node(self, node):
    # Start the HTML rendering for a slide
    self.body.append('<div class="pechakucha-slide">\n')

def depart_pechakucha_slide_node(self, node):
    # End the HTML rendering for a slide
    self.body.append('</div>\n')

def visit_pechakucha_slideshow_node(self, node):
    # Start the HTML rendering for the slideshow container
    self.body.append('<div class="pechakucha-slideshow">\n')

def depart_pechakucha_slideshow_node(self, node):
    # End the HTML rendering for the slideshow container
    self.body.append('</div>\n')

    # Include JavaScript logic for the slideshow
    self.body.append("""
    <script>
        let slideIndex = 0;

        function showSlides() {
            let slides = document.getElementsByClassName("pechakucha-slide");

            for (let i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
            }

            slideIndex++;
            if (slideIndex > slides.length) {
                slideIndex = 1;
            }

            slides[slideIndex - 1].style.display = "block";
            setTimeout(showSlides, 5000); // Change slide every 5 seconds
        }

        // Call the showSlides function when the DOM is ready
        document.addEventListener("DOMContentLoaded", function () {
            let slides = document.getElementsByClassName("pechakucha-slide");
            if (slides.length > 0) {
                showSlides();
            }
        });
    </script>
    """)

# Setup function to register the extension with Sphinx
def setup(app):
    app.add_node(PechakuchaSlide,
                 html=(visit_pechakucha_slide_node, depart_pechakucha_slide_node))
    app.add_node(PechakuchaSlideshow,
                 html=(visit_pechakucha_slideshow_node, depart_pechakucha_slideshow_node))

    app.add_directive('pechakucha_slide', PechakuchaSlideDirective)
    app.add_directive('pechakucha_slideshow', PechakuchaSlideshowDirective)

    return {'version': '0.1', 'parallel_read_safe': True, 'parallel_write_safe': True}
