from abc import ABC, abstractmethod
from tv import AppleTV, TVBase


class RemoteControlBase(ABC):
    @abstractmethod
    def __init__(self):
        self._tv: TVBase = self.get_tv()

    @abstractmethod
    def get_tv(self):
        return NotImplementedError
    
    @abstractmethod
    def tune_channel(self, channel: int):
        self._tv.tune_channel(channel)


class RemoteControl(RemoteControlBase):
    def __init__(self):
        super(RemoteControl, self).__init__()
        self._channel: int = 0

    def get_tv(self):
        return AppleTV()
    
    def tune_channel(self, channel):
        super(RemoteControl, self).tune_channel(channel)
        self._channel = channel

    def next_channel(self):
        self._channel += 1
        self.tune_channel(self._channel)
        
    def previous_channel(self):
        self._channel -= 1
        self.tune_channel(self._channel)