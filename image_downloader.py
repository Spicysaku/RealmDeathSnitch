import os
import requests

def Download_Images() -> None:
    try:
        response = requests.get("https://www.realmeye.com/s/gu/img/sheets.png", stream=True)
        response.raise_for_status()

        file_name = os.path.basename("sheets.png")
        os.makedirs("./images", exist_ok=True)

        with open(os.path.join("./images", file_name), 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Image saved as {file_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}, sheets.png")
    except Exception as e:
            print(f"An error occurred: {e}, sheets.png")

    try:
        response = requests.get("https://www.realmeye.com/s/gu/css/renders.png", stream=True)
        response.raise_for_status()

        file_name = os.path.basename("renders.png")

        with open(os.path.join("./images", file_name), 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Image saved as {file_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}, renders.png")
    except Exception as e:
            print(f"An error occurred: {e}, renders.png")
