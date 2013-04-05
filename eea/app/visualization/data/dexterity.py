""" Dexterity
"""
from zope.component import queryUtility
from plone.dexterity.interfaces import IDexterityFTI
from plone.namedfile.field import NamedBlobFile
from eea.app.visualization.data.data import Data

class Dexterity(Data):
    """ Data adapter for plone.dexterity.content.Container
    """
    @property
    def data(self):
        """ Data to be converted to JSON
        """
        portal_type = getattr(self.context, 'portal_type', '')
        fti = queryUtility(IDexterityFTI, name=name)
        if not fti:
            return super(Dexterity, self).data

        schema = fti.lookupSchema()
        if not schema:
            return super(Dexterity, self).data

        for name in schema.names():
            if not isinstance(schema['file'], NamedBlobFile):
                continue
