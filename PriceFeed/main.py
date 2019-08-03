from iconservice import *
from .exceptions import *
from .interfaces import *
from .utils import *

TAG = 'PriceFeed'


class PriceFeed(IconScoreBase):
    """ PriceFeed SCORE Base implementation """

    # ================================================
    #  DB Variables
    # ================================================
    # The price feed price value
    _VALUE = "VALUE"
    # The timestamp of the latest retrieved value
    _TIMESTAMP = "TIMESTAMP"
    # Score address of the Medianizer
    _MEDIANIZER_SCORE = "MEDIANIZER_SCORE"

    # ================================================
    #  Error codes
    # ================================================
    _SENDER_NOT_SCORE_OWNER = 'SENDER_NOT_SCORE_OWNER'

    # ================================================
    #  Initialization
    # ================================================
    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._value = VarDB(self._VALUE, db, value_type=int)
        self._timestamp = VarDB(self._TIMESTAMP, db, value_type=int)
        self._medianizer_score = VarDB(self._MEDIANIZER_SCORE, db,
                                       value_type=Address)

    def on_install(self, medianizer_score: Address) -> None:
        super().on_install()
        self._value.set(0)
        self._timestamp.set(0)
        self._medianizer_score.set(medianizer_score)

    def on_update(self) -> None:
        super().on_update()

    # ================================================
    #  Checks
    # ================================================
    def _check_is_score_operator(self, address: Address) -> None:
        if self.owner != address:
            raise SenderNotScoreOwner

    # ================================================
    #  External methods
    # ================================================
    @external
    def post(self, value: int) -> None:
        # ==========================
        # Input Checks
        try:
            self._check_is_score_operator(self.msg.sender)
        except SenderNotScoreOwner:
            revert(self._SENDER_NOT_SCORE_OWNER)

        # Update the price
        self._value.set(value)
        self._timestamp.set(self.now())

        # Ask to recalculate the price on the medianizer
        medianizer_score = self.create_interface_score(
            self._medianizer_score.get(),
            MedianizerInterface)
        medianizer_score.poke()

    @external
    def set_medianizer_score(self, score: Address) -> None:
        # ==========================
        # Input Checks
        try:
            self._check_is_score_operator(self.msg.sender)
        except SenderNotScoreOwner:
            revert(self._SENDER_NOT_SCORE_OWNER)

        self._medianizer_score.set(score)

    @external(readonly=True)
    def peek(self) -> str:
        return json_dumps(self._to_dict())

    @external(readonly=True)
    def get_owner(self) -> str:
        return str(self.owner)

    @external(readonly=True)
    def medianizer_score(self) -> str:
        return str(self._medianizer_score.get())

    # ================================================
    #  Private methods
    # ================================================
    def _to_dict(self) -> dict:
        return {
            'value': self._value.get(),
            'timestamp': self._timestamp.get(),
            'medianizer_score': str(self._medianizer_score.get())
        }
