import json
import time
from datetime import date


def load_sessions():
	try:
		with open("focus_log.json", "r", encoding="utf-8") as file:
			return json.load(file)
	except FileNotFoundError:
		return []


def save_sessions(sessions):
	with open("focus_log.json", "w", encoding="utf-8") as file:
		json.dump(sessions, file, indent=2)


def record_session(sessions):
	name = input("Session name: ")
	input("Press Enter to start the session.")
	started_at = time.monotonic()
	session_date = date.today().isoformat()
	input("Press Enter to stop the session.")
	minutes = round((time.monotonic() - started_at) / 60, 1)

	session = {"name": name, "minutes": minutes, "date": session_date}
	sessions.append(session)
	save_sessions(sessions)
	print(f"Recorded {name}: {minutes} min.")


def print_summary(sessions):
    if not sessions:
        print("No focus sessions logged today.")
        return

    totals = {}
    for session in sessions:
        name = session["name"]
        totals[name] = totals.get(name, 0) + session["minutes"]

    for name, minutes in totals.items():
        print(f"{name}: {minutes} min")

    print(f"Total: {sum(totals.values())} min")

sessions = load_sessions()


while True:
	print("\n1. Start a focus session")
	print("2. Show today's summary")
	print("3. Quit")

	choice = input("Choose an option: ")

	if choice == "1":
		record_session(sessions)
	elif choice == "2":
		print("Today's summary (placeholder).")
	elif choice == "3":
		break
	else:
		print("Not a valid choice")
