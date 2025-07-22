# roles-and-accesses.py

# Example of use:
"""
admin_users = [
    "123456789012345678",  # Example user ID
    # Add more user IDs here
]

admin_role = "123456789012345678" # Example role ID
"""

# List of user IDs with full admin access to all commands including admin-level commands (e.g., /ram set, /restart) 
# If left empty, any user can use these commands—unless admin_role is not empty.
admin_users = []

# Role IDs allowed to use all commands including admin-level commands (e.g., /ram set, /restart) 
# If left empty, any user can use these commands—unless admin_users is not empty.
admin_role = ""

# Role IDs allowed to use only informational commands (e.g., /server, /ram get)
#If leave blank, any user will have access to these commands
info_role = ""
