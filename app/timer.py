import time
from datetime import datetime, timedelta

interval_minutes = 1

def minutes_until_next_time():
  now = datetime.now()
  current_minute = now.minute
  current_minute_floor = int(current_minute / interval_minutes) * interval_minutes
  target_minute = current_minute_floor + interval_minutes
  advance_minutes = target_minute - current_minute
  return advance_minutes

def sleep_until_next_time():
  time.sleep(minutes_until_next_time() * 60)
