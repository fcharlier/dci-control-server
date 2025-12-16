# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2023 Red Hat, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


def test_list_jobstates_return_files_and_tasks_with_tasks_key(
    client_user1, team1_job_id, team1_jobstate_file_id, team1_jobstate_task_id
):
    list_jobstates = client_user1.get(f"/api/v2/jobs/{team1_job_id}/jobstates")
    assert list_jobstates.status_code == 200

    jobstates = list_jobstates.data["jobstates"]
    tasks = jobstates[0]["tasks"]
    assert len(tasks) == 2
    for file in tasks:
        assert file["id"] in [team1_jobstate_file_id, team1_jobstate_task_id]


def test_get_files_by_job_id_doesnt_return_jobstate_file_aka_tasks_on_v2_endpoint(
    client_user1, team1_job_id, team1_job_file_id, team1_jobstate_file_id
):
    file_from_job = client_user1.get("/api/v2/jobs/%s/files" % team1_job_id)
    assert file_from_job.status_code == 200
    assert file_from_job.data["_meta"]["count"] == 1
