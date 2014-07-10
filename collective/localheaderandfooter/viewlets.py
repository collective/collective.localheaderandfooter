#-*- coding: utf-8 -*-

from zope.dottedname.resolve import resolve
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets import ViewletBase

from .utils import get_local_header
from .utils import get_local_footer


class HeaderViewlet(ViewletBase):
    """A simple viewlet which renders an header
    """

    default_template_name = 'portal_header.pt'

    @property
    def default_path(self):
        mod = resolve('plone.app.layout.viewlets')
        path = '/'.join(
            mod.__path__ + [self.default_template_name]
        )
        return path

    @property
    def index(self):
        return ViewPageTemplateFile(self.default_path)

    def update(self):
        self.local = self.get_local()

    def render(self):
        if self.local:
            return self.local
        return self.index(self)

    def get_local(self):
        return get_local_header(self.context,
                                self.request)


class FooterViewlet(HeaderViewlet):
    """The footer viewlet
    """

    default_template_name = "footer.pt"

    def get_local(self):
        return get_local_footer(self.context,
                                self.request)
