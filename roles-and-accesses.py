# roles-and-accesses.py

# Example of use:
"""
admin_users = [
    "12345678901234567",  # Example user ID
    # Add more user IDs here
]
"""

# List of user IDs with full admin access to all commands including admin-level commands (e.g., /ram set, /restart) 
# If left empty, any user can use these commands—unless admin_roles is not empty.
admin_users = []

# Role IDs allowed to use all commands including admin-level commands (e.g., /ram set, /restart) 
# If left empty, any user can use these commands—unless admin_users is not empty.
admin_roles = []

# Role IDs allowed to use only informational commands (e.g., /server, /ram get)
#If leave blank, any user will have access to these commands
info_roles = []
