#
# -------------------------------------------------------------------------
#   Copyright (c) 2019 AT&T Intellectual Property
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# -------------------------------------------------------------------------
#
class MemFilter(object):

    def __init__(self):
        self.name = "mem"

        self.status = None

    def init_condition(self):
        self.status = None

    def check_pre_condition(self, _level, _v, _avail_hosts, _avail_groups):
        return True

    def filter_candidates(self, _level, _v, _candidate_list):
        candidate_list = []

        for c in _candidate_list:
            if self._check_candidate(_level, _v, c):
                candidate_list.append(c)

        return candidate_list

    def _check_candidate(self, _level, _v, _candidate):
        """Only return hosts with sufficient available RAM."""

        requested_ram = _v.mem   # MB
        usable_ram = _candidate.get_mem(_level)

        # TODO: need to check against original mem_cap?
        # Do not allow an instance to overcommit against itself,
        # only against other instances.
        # if not total_ram >= requested_ram:
        #     return False

        if not usable_ram >= requested_ram:
            return False

        return True
