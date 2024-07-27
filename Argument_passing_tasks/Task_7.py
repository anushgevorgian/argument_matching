def log_messages(severity, *args, **kwargs):
    log_entry = f"Severity: -- {severity} --\n"

    if 'timestamp' in kwargs:
        log_entry += f"Timestamp: {kwargs['timestamp']}\n"
    if 'user' in kwargs:
        log_entry += f"User: {kwargs['user']}\n"

    log_entry += "Messages:\n"
    for message in args:
        log_entry += f"-- {message} --\n"

    print(log_entry)

log_messages(
    "ERROR",
    "Wrong password.",
    "CapsLock is on.",
    timestamp="2024-07-27 14:30:00",
    user="anush"
)
