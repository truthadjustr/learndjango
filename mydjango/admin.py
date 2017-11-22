from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

class MyAdminSite(AdminSite):
    # text to put at each page's <title>
    site_title = ugettext_lazy('Deca Homes site admin')

    # The text to put at the top of each admin page, as an <h1>
    site_header = ugettext_lazy('DecaHomes Administration')

    # Text to put at the top of the admin index page
    index_title = ugettext_lazy('Prime administration')

my_admin_site = MyAdminSite()
