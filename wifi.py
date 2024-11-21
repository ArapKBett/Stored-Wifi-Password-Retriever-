import subprocess

def get_wifi_passwords():
    # Run the command to get Wi-Fi profiles
    profiles_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    
    profiles = [line.split(":")[1][1:-1] for line in profiles_data if "All User Profile" in line]
    
    wifi_passwords = {}
    
    for profile in profiles:
        # Run the command to get the password for each profile
        profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
        
        password_line = [line for line in profile_info if "Key Content" in line]
        
        if password_line:
            password = password_line[0].split(":")[1][1:-1]
        else:
            password = None
        
        wifi_passwords[profile] = password
    
    return wifi_passwords

if __name__ == "__main__":
    passwords = get_wifi_passwords()
    for profile, password in passwords.items():
        print(f"Profile: {profile}, Password: {password}")
