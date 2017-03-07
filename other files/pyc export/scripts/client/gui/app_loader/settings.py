# Embedded file name: scripts/client/gui/app_loader/settings.py


class GUI_GLOBAL_SPACE_ID(object):
    UNDEFINED = 0
    WAITING = 1
    INTRO_VIDEO = 2
    LOGIN = 3
    LOBBY = 4
    BATTLE_LOADING = 5
    BATTLE = 6


class DISCONNECT_REASON(object):
    UNDEFINED = 0
    REQUEST = 1
    EVENT = 2
    KICK = 3
    ERROR = 4


class APP_STATE_ID(object):
    NOT_CREATED = 0
    INITIALIZING = 1
    INITIALIZED = 2


class APP_NAME_SPACE(object):
    SF_LOBBY = 'scaleform/lobby'
    SF_BATTLE = 'scaleform/battle'
    SF_LOGITECH = 'scaleform/logiTech'
    RANGE = (SF_LOBBY, SF_BATTLE, SF_LOGITECH)
