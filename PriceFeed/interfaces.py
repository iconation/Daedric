from iconservice import *

# ================================================
#  Medianizer SCORE interface
# ================================================


class MedianizerInterface(InterfaceScore):
    @interface
    def poke(self) -> None:
        pass
