# *****************************************************************************
# Copyright (C) 2023 INAF
# This software is distributed under the terms of the BSD-3-Clause license
#
# Authors:
# Ambra Di Piano <ambra.dipiano@inaf.it>
# *****************************************************************************

import pytest
from deeprta.hello import hello

@pytest.mark.tmp
def test_hello():
    assert hello() == 'hello world'
