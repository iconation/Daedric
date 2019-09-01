# -*- coding: utf-8 -*-

# Copyright 2019 ICONation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from iconservice import *
from .version import *
from .checks import *

TAG = 'Daedric'
VERSION = '1.1.0'


class Daedric(IconScoreBase):
    """ Daedric SCORE Base implementation """

    # ================================================
    #  DB Variables
    # ================================================
    # The price feed price value
    _VALUE = "VALUE"
    # The timestamp of the latest retrieved value
    _TIMESTAMP = "TIMESTAMP"
    # Ticker name, it needs to be the same than the medianizer
    # if you want to participate to the consensus
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
        Version.set(self.db, VERSION)

    def on_update(self) -> None:
        super().on_update()
        Version.set(self.db, VERSION)

    # ================================================
    #  External methods
    # ================================================
    @external
    @only_owner
    @catch_error
    def post(self, value: int) -> None:
        """ Set a new price to the feed. It replaces the previous one."""
        self._value.set(value)
        self._timestamp.set(self.now())

    @external
    @only_owner
    @catch_error
    def set_ticker_name(self, ticker_name: str) -> None:
        """ Set a new ticker name. It replaces the previous one."""
        self._ticker_name.set(ticker_name)

    # ==== ReadOnly methods =============================================
    @external(readonly=True)
    @catch_error
    def peek(self) -> dict:
        """ Get the current Daedric state."""
        return self._serialize()

    # ================================================
    #  Private methods
    # ================================================
    def _serialize(self) -> dict:
        return {
            'value': self._value.get(),
            'timestamp': self._timestamp.get(),
            'ticker_name': self._ticker_name.get()
        }
