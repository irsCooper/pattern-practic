from abc import ABC, abstractmethod


class TVBase(ABC):
    @abstractmethod
    def tune_channel(self, channel: int):
        raise NotImplementedError
    

class SonyTV(TVBase):
    def tune_channel(self, channel: int):
        print(f"Sony TV: selected {channel} channel")


class AppleTV(TVBase):
    def tune_channel(self, channel: int):
        print(f"Apple TV: selected {channel} channel")