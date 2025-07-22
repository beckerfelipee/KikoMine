# Configure discord permissions levels for the bot usage

# Example of use:
"""
admin_users = [
    123456789012345678,  # Example Discord user ID
    # Add more user IDs here
]

admin_role = 123456789012345678 # Example Discord role ID
"""

# List of user IDs with full admin access to all commands including admin-level commands (e.g., /ram set, /restart) 
# If left empty, any user can use these commands—unless admin_role is not empty.
# list[int]
admin_users = [
    434795654527713291, # Kikope
    421014073476382733, # Linho
    461683330585460757, # Heez
    ]

# Role IDs allowed to use all commands including admin-level commands (e.g., /ram set, /restart) 
# If left None, any user can use these commands—unless admin_users is not empty.
# int or None
admin_role = 1216457081876385884 # KikoMine

# Role IDs allowed to use only informational commands (e.g., /server, /ram get)
#If left None, any user will have access to these commands
# int or None
info_role = None

