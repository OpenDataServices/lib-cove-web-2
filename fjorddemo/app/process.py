import os

from libfjordweb.process.common_tasks.task_with_state import TaskWithState


class DetailsOnJSON(TaskWithState):
    """"""

    state_filename: str = "details_on_json.json"

    def process_get_state(self, process_data: dict):

        out: dict = {}

        supplied_data_json_files = [
            i for i in self.supplied_data_files if i.content_type == "application/json"
        ]
        if len(supplied_data_json_files) == 1:
            out["data_size"] = os.path.getsize(
                supplied_data_json_files[0].upload_dir_and_filename()
            )
        else:
            raise Exception("Can't find JSON original data!")

        return out, process_data
