# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CyberSportRespawnViewMeta.py
from gui.Scaleform.framework.entities.View import View

class CyberSportRespawnViewMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def as_setMapBGS(self, imgsource):
        if self._isDAAPIInited():
            return self.flashObject.as_setMapBG(imgsource)

    def as_changeAutoSearchStateS(self, value):
        """
        :param value: Represented by AutoSearchVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_changeAutoSearchState(value)

    def as_hideAutoSearchS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideAutoSearch()
