import time
import random

def simulate_action(action_name, steps=4, step_duration=1):
    print(f"\n{action_name}...", end="", flush=True)
    for _ in range(steps):
        time.sleep(step_duration)  # Simulate the action taking time
        print(".", end="", flush=True)
    print("Done.")

def get_user_details():
    user_details = {}
    user_details['name'] = input("Enter your name: ")
    # user_details['email'] = input("Enter your email: ")
    user_details['last_called'] = input("Enter the last person you called: ")
    return user_details

def install_tracking_package(phone_number):
    print(f"\nInitiating tracking package installation on {phone_number}.")
    simulate_action("Connecting to the device", 3, 1)
    simulate_action("Installing tracking package", 15, 1)
    simulate_action("Finalizing installation", 20, 1)
    print("Installation successful. Tracking activated.")

def simulate_tracking_sequence():
    progress_bar_width = 20
    for i in range(progress_bar_width + 1):
        progress = i * 25
        print(f"\rTracking progress: [{'#' * i}{' ' * (progress_bar_width - i)}] {progress}% complete", end="", flush=True)
        time.sleep(0.3)  # Simulate progress update delay
    print()  # Move to next line after progress bar completion

    simulate_action("Locating network", 5, 0.5)
    simulate_action("Encrypting connection for data retrieval", 6, 0.5)
    simulate_action("Retrieving location data", 6, 0.5)
    print("\nLocation update: The phone is in Nairobi, Umoja location.")
    simulate_action("Attempting to secure device", 4, 0.5)
    print("\nWarning: Device has been flushed by the user.")
    simulate_action("Attempting to bypass flush", 3, 0.5)
    print("\nError: Multiple security breaches detected.")
    simulate_action("Retrying connection", 3, 0.75)
    print("\nCritical Error: Device has been switched off. Unable to regain connection.")
    simulate_action("Retrying connection", 3, 0.75)
    print("\nCritical Error: Device has been switched off. Unable to regain connection.")
    simulate_action("Retrying connection", 3, 0.75)
    print("\nCritical Error: Device has flushed switched off. Unable to regain connection.")
    

def track_phone(phone_number):
    print(f"\nTracking phone: {phone_number}")
    simulate_tracking_sequence()
    print("\nTracking complete. Unfortunately, the device is now offline and can't be tracked further.")
    print("Last known location: Umoja, Nairobi")
    print("The device was switched off at 3:59 AM yesterday.")
    print("Latitude: -1.286389, Longitude: 36.817223")  # Fake coordinates for Umoja, Nairobi

def main():
    print("Welcome to the Enhanced KENYAN Phone Tracker")
    user_details = get_user_details()  # Collect user details
    print(f"\nHello, {user_details['name']}. Let's start tracking.")
    phone_number = input("Enter the phone number to track: ")
    install_tracking_package(phone_number)
    track_phone(phone_number)

if __name__ == "__main__":
    main()
