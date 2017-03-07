# Embedded file name: scripts/client/gui/prb_control/entities/base/unit/listener.py
from gui.prb_control.entities.base.listener import IPrbListener

class IUnitIntroListener(IPrbListener):
    """
    Unit intro events listener interface
    """

    def onUnitAutoSearchStarted(self, timeLeft):
        """
        Establishes a listener to respond when UnitIntroEntity receives
        event g_playerEvents.onEnqueuedUnitAssembler.
        Args:
            timeLeft: time left in autosearch state
        """
        pass

    def onUnitAutoSearchFinished(self):
        """
        Establishes a listener to respond when UnitIntroEntity receives
        event g_playerEvents.onDequeuedUnitAssembler.
        """
        pass

    def onUnitAutoSearchSuccess(self, acceptDelta):
        """
        Establishes a listener to respond when UnitIntroEntity receives
        autoSearch result.
        Args:
            acceptDelta: accept time left
        """
        pass

    def onUnitBrowserErrorReceived(self, errorCode):
        """
        Establishes a listener to respond when UnitEntity receives unit
        browser error from server.
        Args:
            errorCode: error code
        """
        pass


class IUnitListener(IUnitIntroListener):

    def onUnitFlagsChanged(self, flags, timeLeft):
        """
        Establishes a listener to respond when UnitEntity receives new
        state of unit.
        Args:
            flags: flags of unit
            timeLeft: time left in search/queue
        """
        pass

    def onUnitPlayerStateChanged(self, pInfo):
        """
        Establishes a listener to respond when UnitEntity receives new
        player's ready state.
        Args:
            pInfo: player's info that was changed
        """
        pass

    def onUnitPlayerRolesChanged(self, pInfo, pPermissions):
        """
        Establishes a listener to respond when UnitEntity receives new
        roles for player.
        Args:
            pInfo: player's info that changed
            pPermissions: new permissions
        """
        pass

    def onUnitPlayerOnlineStatusChanged(self, pInfo):
        """
        Establishes a listener to respond when UnitEntity receives
        status (offline/online) changed for player.
        Args:
            pInfo: player's info that changed
        """
        pass

    def onUnitPlayerBecomeCreator(self, pInfo):
        """
        Establishes a listener to respond when UnitEntity receives
        that player become creator.
        Args:
            pInfo: player's info that was changed
        """
        pass

    def onUnitPlayerEnterOrLeaveArena(self, pInfo):
        """
        Establishes a listener to respond when UnitEntity receives
        when player enter or leave arena.
        Args:
            pInfo: player's info that was changed
        """
        pass

    def onUnitRosterChanged(self):
        """
        Establishes a listener to respond when UnitEntity receives roster
        change.
        """
        pass

    def onUnitMembersListChanged(self):
        """
        Establishes a listener to respond when UnitEntity receives members
        list update (remove or add member).
        """
        pass

    def onUnitPlayerAdded(self, pInfo):
        """
        Establishes a listener to respond when UnitEntity receives
        when player added.
        Args:
            pInfo: player's info that was added
        """
        pass

    def onUnitPlayerInfoChanged(self, pInfo):
        """
        Establishes a listener to respond when UnitEntity receives
        when player's info changes.
        Args:
            pInfo: player's info that was updated
        """
        pass

    def onUnitPlayerRemoved(self, pInfo):
        """
        Establishes a listener to respond when UnitEntity receives
        when player removed.
        Args:
            pInfo: player's info that was removed
        """
        pass

    def onUnitPlayersListChanged(self):
        """
        Establishes a listener to respond when UnitEntity receives players
        list update (remove or add player).
        """
        pass

    def onUnitVehiclesChanged(self, dbID, vInfos):
        """
        Establishes a listener to respond when UnitEntity receives new
        vehicle for player.
        Args:
            dbID: player's database ID.
            vInfos: vehicles infos list
        """
        pass

    def onUnitPlayerVehDictChanged(self, pInfo):
        """
        Establishes a listener to respond when UnitEntity receives new
        dictionary of vehicles (in inventory) for player.
        Args:
            pInfo: player's info that was changed
        """
        pass

    def onUnitSettingChanged(self, opCode, value):
        """
        Establishes a listener to respond when UnitEntity receives new
        setting value for unit.
        Args:
            opCode: operation code from UNIT_OP
            value: new value for given setting
        """
        pass

    def onUnitRejoin(self):
        """
        Establishes a listener to respond when UnitEntity rejoins to itself.
        """
        pass

    def onUnitErrorReceived(self, errorCode):
        """
        Establishes a listener to respond when UnitEntity receives unit error
        from server.
        Args:
            errorCode: error code, one from UNIT_ERROR
        """
        pass

    def onUnitExtraChanged(self, extra):
        """
        Establishes a listener to respond when UnitEntity receives update
        for unit extra from server.
        Args:
            extra: new unit extra data
        """
        pass

    def onUnitCurfewChanged(self):
        """
        Establishes a listener to respond when UnitEntity receives curfew update
        """
        pass
