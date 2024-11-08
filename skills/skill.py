import requests


class SkillManager:

    def __init__(self, instance_name, access_token):
        self.instance_name = instance_name
        self.access_token = access_token

    def add_skill(self, agent_id, queue_id, priority="1"):
        # add skill to agent
        url = (
            "https://"
            + self.instance_name
            + f"-api.aswat.co/admin/skills/agents/{agent_id}/"
        )
        payload = {"queue": queue_id, "priority": priority}
        headers = {
            "access_token": self.access_token,
            "Content-Type": "application/json",
        }

        response = requests.post(url, headers=headers, json=payload)
        return response

    def remove_skill(self, agent_id, queue_id):
        #  remove skill from agent
        url = (
            "https://"
            + self.instance_name
            + f"-api.aswat.co/admin/skills/agents/{agent_id}/{queue_id}"
        )
        headers = {
            "access_token": self.access_token,
            "Content-Type": "application/json",
        }

        response = requests.delete(url, headers=headers)
        return response

    def get_skills(self):
        url = (
            "https://" + self.instance_name + f"-api.aswat.co/admin/skills/listQueues/"
        )
        headers = {
            "access_token": self.access_token,
            "Content-Type": "application/json",
        }
        print(url)

        response = requests.get(url, headers=headers)
        return response
