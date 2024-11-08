import requests
import pandas as pd


class QueueManager:

    def __init__(self, instance_name, access_token):
        self.instance_name = instance_name
        self.access_token = access_token

    def add_queues(self, days=[], time="10:00-22:00"):
        # add queues from csv file

        headers = {
            "access_token": self.access_token,
            "Content-Type": "application/json",
        }

        with open(self.file_path, "r") as file:
            df = pd.read_csv(self.file_path)
            print(df)
            for index, row in df.iterrows():
                # Queue name
                name = row["Queue_Name"]
                # Waiting audio music
                moh = row["MOH"]
                # strategyType
                strategy = row["Strategy"]
                # language
                lang = row["lang"]
                # nonWorkingHoursDID is Transfer to Call Center Number
                did = row["did"]

                payload = {
                    "moh": moh,
                    "announcementAudio": None,
                    "name": name,
                    "strategyType": strategy,
                    "announcementType": "position",
                    "priority": "101",
                    "language": lang,
                    "surveyRequired": True,
                    "nonWorkingHoursDID": did,
                    "timeslots": [
                        {
                            "days": days,
                            "time": time,
                        }
                    ],
                    "waitTimeoutDID": "",
                    "maxWaitTime": 0,
                }
                # payload='name=' + row[1] + '&strategyType=longest-idle-agent&priority=101&moh=' + moh + '&announcementType=position&surveyRequired=false'
                url = "https://" + self.instance_name + "-api.aswat.co/admin/queues"
                print("Processing: ", name)
                response = requests.post(url, headers=headers, json=payload)
                print("Status is: ", str(response.status_code))
                print("Response Text is: ", response.text, "\n")
                # break

    def get_queues_count(self):
        url = (
            "https://" + self.instance_name + "-api.aswat.co/admin/queues/count?search"
        )
        headers = {"access_token": self.access_token}
        response = requests.get(url, headers=headers)
        print(response.json())
        return response.json()["content"]

    def get_queues(self):
        pass

    def get_queue_by_name(self):
        pass


instance_name = "ivr-test-poc"
access_token = "f9a8ac51-817a-4940-bc1f-dde76e1b946f"
# file_path = "./queue-list.csv"

# add_queues(instance_name, access_token, file_path)
queue_manager = QueueManager(instance_name, access_token)
print(queue_manager.get_queues_count())
