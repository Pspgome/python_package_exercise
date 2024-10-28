# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

import pytest
import numpy as np
import sys
import os
# Add working directory to path. Python doesn't like relative imports in scripts, otherwise it'd be best to use that
sys.path.append(os.getcwd())
from basic_sort_UNIQUE_SUFFIX.int_sort import bubble, quick, insertion

def is_sorted(int_list):
    """
    Testing oracle.
    """
    # Iterate through the list, checking each element is greater than or equal to the previous
    for x in range(len(int_list) - 1):
        if int_list[x] > int_list[x + 1]:
            return False
    
    return True

@pytest.fixture
def int_lists():
    # fixture which creates testing data for all tests
    return [[3,2,1],
	        [1,1,1],
			np.random.randint(low=-10, high=200, size=5)] 
    
def test_bubble(int_lists):
    for int_list in int_lists:
        assert is_sorted(bubble(int_list))

def test_quick(int_lists):
    for int_list in int_lists:
        assert is_sorted(quick(int_list))

def test_insertion(int_lists):
    for int_list in int_lists:
        assert is_sorted(insertion(int_list))