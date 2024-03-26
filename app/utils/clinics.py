import requests

def get_clinics():
    api_url = "https://tight-similarly-chigger.ngrok-free.app/api/getClinics"

    try:
        # Make the POST request with an empty JSON body
        response = requests.post(api_url, json={})

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract clinic information from the response
            clinics = data.get("message", [])
            return clinics
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []

    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
def get_clinic_schedule():
    return

def add_appointment():
    return

def get_user_info_and_status():
    return

def get_messages():
    return

def add_message():
    return

