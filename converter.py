# pip install ics
# pip install openpyxl

from ics import Calendar
from openpyxl import Workbook
from sys import argv

def convert(source_path: str, target_path: str):
    with open(source_path, 'r') as f:
        ics_content = f.read()
        cal = Calendar(ics_content)
    
    team_name = cal.extra[0].value[12:] # Termine von ...


    wb = Workbook()
    ws = wb.active
    ws.append(["Gegner", "Heimspiel", "Start-Datum", "Startzeit", "End-Datum", "Endzeit", "Adresse", "Bemerkung"])

    for event in cal.events:
        [team1, team2] = event.name.split(" vs. ")
        is_home = team1 == team_name
        ws.append([team2 if is_home else team1, "Ja" if is_home else "Nein", event.begin.date(), event.begin.time(), event.end.date(), event.end.time(), event.location, event.description])
    
    wb.save(target_path)


if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: python converter.py <source_path> <target_path>")
        exit(1)

    convert(source_path=argv[1], target_path=argv[2])