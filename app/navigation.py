from app import nav
from flask_nav.elements import Navbar, View, Link, Separator


topbar = Navbar('',
    View('Home', 'index'),
    View('Projects', 'projects'),
    View('Contact', 'contact'),
    Separator(),
    Link('', 'https://github.com/6ixBit'), navbar

)

nav.register_element('top', topbar)
