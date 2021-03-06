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
class DiversityFilter(object):

    def __init__(self):
        self.name = "diversity"

        self.diversity_list = []

        self.status = None

    def init_condition(self):
        self.diversity_list = []
        self.status = None

    def check_pre_condition(self, _level, _v, _avail_hosts, _avail_groups):
        if len(_v.diversity_groups) > 0:
            for _, div_group in _v.diversity_groups.items():
                if div_group.level == _level:
                    self.diversity_list.append(div_group.vid)

        if len(self.diversity_list) > 0:
            return True
        else:
            return False

    def filter_candidates(self, _level, _v, _candidate_list):
        candidate_list = []

        for c in _candidate_list:
            if self._check_candidate(_level, c):
                candidate_list.append(c)

        return candidate_list

    def _check_candidate(self, _level, _candidate):
        """Filter based on named diversity groups."""

        memberships = _candidate.get_memberships(_level)

        for diversity_id in self.diversity_list:
            for gk, gr in memberships.items():
                if gr.group_type == "diversity" and gk == diversity_id:
                    return False

        return True
