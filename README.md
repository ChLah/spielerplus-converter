# Spielerplus MyTischtennis Converter

This tool converts your exported appointments from [MyTischtennis](https://www.mytischtennis.de) to an xlsx file that can be imported into your [SpielerPlus](https://www.spielerplus.de) team calendar.\
The format of the xlsx file can be found in [docs](/docs/sample.xlsx)

To import your appointments, do the following:

### Export Appointments

Go to MyTischtennis under the section "click-TT" and click on your team. From there you can click the button "Termine herunterladen".\
This should give you an ics file of all your matches for this season.

### Convert files

You can open the resulting xlsx file and check your appointments manually. If needed you can also change some cells.

### Import Appointments

Go to Spielerplus and click on calendar / create event or use this link: [here](https://www.spielerplus.de/import/create-game). Login if needed and upload your file.\
You now need to map the columns of the imported file with the required. Atm the following mappings are used:

* Gegner -> Gegner
* Heimspiel -> Heimspiel
* Start-Datum -> Start-Datum
* Startzeit -> Startzeit
* End-Datum -> End-Datum
* Endzeit -> Endzeit
* Adresse -> Gelände / Räumlichkeiten \
(alternativelly you can also tick the "Adressen importieren" box up top and use the column "Adresse", but you then need to map to existing locations)