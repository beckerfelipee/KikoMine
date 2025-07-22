# roles-and-accesses.py

#If leave blank, any user will have access to the commands

# Example of use:
"""
admin_users = [
    "12345678901234567",  # Example user ID
    # Add more user IDs here
]
"""

# List of user IDs with full admin access to all commands including admin-level commands (e.g., /ram set, /restart) 
admin_users = []

# Role IDs allowed to use all commands including admin-level commands (e.g., /ram set, /restart) 
admin_roles = []

# Role IDs allowed to use informational commands (e.g., /server, /ram get)
info_roles = []
