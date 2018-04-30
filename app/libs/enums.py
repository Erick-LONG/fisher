from enum import Enum


class PendingStatus(Enum):
    '''交易4种状态'''
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4