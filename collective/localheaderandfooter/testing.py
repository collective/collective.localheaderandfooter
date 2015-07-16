# -*- coding: utf-8 -*-

from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.localheaderandfooter
        self.loadZCML(package=collective.localheaderandfooter)

        if 'virtual_hosting' not in app.objectIds():
            # If ZopeLite was imported, we have no default virtual
            # host monster
            from Products.SiteAccess.VirtualHostMonster \
                import manage_addVirtualHostMonster
            manage_addVirtualHostMonster(app, 'virtual_hosting')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'collective.localheaderandfooter:default')
        self.applyProfile(portal, 'collective.localheaderandfooter:testfixture')


FIXTURE = Fixture()


INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='collective.localheaderandfooter:Integration',
)

FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE, z2.ZSERVER_FIXTURE),
    name='collective.localheaderandfooter:Functional',
)

ROBOT_TESTING = FunctionalTesting(
    bases=(FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE, z2.ZSERVER_FIXTURE),
    name='collective.localheaderandfooter:Robot')
