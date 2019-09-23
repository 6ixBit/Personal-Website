from app import nav
from flask_nav.elements import Navbar, View

topbar = Navbar('',
    View('Home', 'index'),
    View('Projects', 'projects'),
    View('Contact', 'contact')
)

nav.register_element('top', topbar)