from iconservice import *
from .exceptions import *

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
    # Ticker name (for display purpose)
    _TICKER_NAME = 'TICKER_NAME'

    # ================================================
    #  Initialization
    # ================================================
    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._value = VarDB(self._VALUE, db, value_type=int)
        self._timestamp = VarDB(self._TIMESTAMP, db, value_type=int)
        self._ticker_name = VarDB(self._TICKER_NAME, db, value_type=str)

    def on_install(self, ticker_name: str) -> None:
        super().on_install()
        self._value.set(0)
        self._timestamp.set(0)
        self._ticker_name.set(ticker_name)

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
        """ Set a new price to the feed. It replaces the previous one."""
        # ==========================
        # Input Checks
        try:
            self._check_is_score_operator(self.msg.sender)
        except (SenderNotScoreOwner) as error:
            revert(error.message)

        # Update the price
        self._value.set(value)
        self._timestamp.set(self.now())

    @external
    def set_ticker_name(self, ticker_name: str) -> None:
        # ==========================
        # Input Checks
        try:
            self._check_is_score_operator(self.msg.sender)
        except (SenderNotScoreOwner) as error:
            revert(error.message)

        # ==========================
        # Process
        self._ticker_name.set(ticker_name)

    # ==== ReadOnly methods =============================================

    @external(readonly=True)
    def peek(self) -> str:
        """ Get the current price stored in the price feed."""
        return json_dumps(self._to_dict())

    # ================================================
    #  Private methods
    # ================================================
    def _to_dict(self) -> dict:
        return {
            'value': self._value.get(),
            'timestamp': self._timestamp.get(),
            'ticker_name': self._ticker_name.get()
        }
