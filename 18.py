has_keycard = True
knows_password = False
is_admin = False

if is_admin or (has_keycard and knows_password):
    print("Door unlocked")
else:
    print("access denied")
