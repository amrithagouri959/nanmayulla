from django import template
from django.utils import timezone
from datetime import timedelta

register = template.Library()

@register.filter
def format_session_time(start_time, end_time=None):
    """
    Formats start and end time in a human-readable format like "3 PM to 5 PM".
    If end_time is None, it displays "Ongoing".
    """
    if not start_time:
        return ''

    # Format the start time
    start_time_formatted = start_time.strftime("%-I:%M %p")  # "3:00 PM"

    if end_time:
        # Format the end time
        end_time_formatted = end_time.strftime("%-I:%M %p")  # "5:00 PM"
        return f"{start_time_formatted} - {end_time_formatted}"
    else:
        return f"{start_time_formatted} - Ongoing..."

@register.filter
def format_duration(duration):
    """
    Formats duration in a human-readable format like "2 hours 30 minutes 5 seconds".
    """
    if isinstance(duration, timedelta):
        # Get total seconds
        total_seconds = int(duration.total_seconds())
        # Calculate hours, minutes, and seconds
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Format the output
        parts = []
        if hours > 0:
            parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
        if minutes > 0:
            parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
        if seconds > 0:
            parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")

        return ' '.join(parts)
    return 'Ongoing'
