# encoding: utf-8

"""
lxml custom element classes for picture-related XML elements.
"""

from __future__ import absolute_import

from lxml import objectify

from pptx.oxml import element_class_lookup, nsdecls, oxml_fromstring
from pptx.spec import nsmap


class CT_Picture(objectify.ObjectifiedElement):
    """
    ``<p:pic>`` element, which represents a picture shape (an image placement
    on a slide).
    """
    _pic_tmpl = (
        '<p:pic %s>\n'
        '  <p:nvPicPr>\n'
        '    <p:cNvPr id="%s" name="%s" descr="%s"/>\n'
        '    <p:cNvPicPr>\n'
        '      <a:picLocks noChangeAspect="1"/>\n'
        '    </p:cNvPicPr>\n'
        '    <p:nvPr/>\n'
        '  </p:nvPicPr>\n'
        '  <p:blipFill>\n'
        '    <a:blip r:embed="%s"/>\n'
        '    <a:stretch>\n'
        '      <a:fillRect/>\n'
        '    </a:stretch>\n'
        '  </p:blipFill>\n'
        '  <p:spPr>\n'
        '    <a:xfrm>\n'
        '      <a:off x="%s" y="%s"/>\n'
        '      <a:ext cx="%s" cy="%s"/>\n'
        '    </a:xfrm>\n'
        '    <a:prstGeom prst="rect">\n'
        '      <a:avLst/>\n'
        '    </a:prstGeom>\n'
        '  </p:spPr>\n'
        '</p:pic>' % (nsdecls('a', 'p', 'r'), '%d', '%s', '%s', '%s',
                      '%d', '%d', '%d', '%d')
    )

    @staticmethod
    def new_pic(id_, name, desc, rId, left, top, width, height):
        """
        Return a new ``<p:pic>`` element tree configured with the supplied
        parameters.
        """
        xml = CT_Picture._pic_tmpl % (id_, name, desc, rId,
                                      left, top, width, height)
        pic = oxml_fromstring(xml)

        objectify.deannotate(pic, cleanup_namespaces=True)
        return pic


p_namespace = element_class_lookup.get_namespace(nsmap['p'])
p_namespace['pic'] = CT_Picture
