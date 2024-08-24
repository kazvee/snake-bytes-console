def input_is_valid(user_input):
  if not user_input.strip():
    return False
  if user_input.isdigit():
    return False
  return True