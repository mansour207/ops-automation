import requests
import glob
import os


def upload_audios(instance_name, access_token, folder_path):

    headers = {"access_token": access_token}
    url = "https://" + instance_name + "-api.aswat.co/uploader/storage/audio"

    audios = list(glob.glob(folder_path + "**/*.mp3", recursive=True))
    results = {}

    for audio_file_path in audios:
        with open(audio_file_path, "rb") as f:
            # file_binary = f.read()
            original_name = os.path.basename(audio_file_path)
            files = {"file": (original_name, f, "audio/mpeg")}
            response = requests.post(url, headers=headers, files=files)

        print("Status is: ", str(response.status_code))
        print("Response Text is: ", response.json(), "\n")
        result = response.json()
        results[result["content"]["originalName"].split(".")[0]] = (
            "/" + result["content"]["name"]
        )

    print(results)
    return results


instance_name = "ajex2-sandbox"
access_token = "c212edc1-ffe9-4613-8ae7-bebb8980b41f"
folder_path = "C:\\work\\Ziwo\\projects\\ajex\\IVR 3\\"

upload_audios(instance_name, access_token, folder_path)
