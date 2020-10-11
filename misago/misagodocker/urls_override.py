from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    # menu item created in admincp
    url(r'^guildline$', TemplateView.as_view(template_name="misago/guildline.html"), name='guildline'),
]