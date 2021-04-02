# psafe3-to-keepass-csv

Export Password Safe v3 files as KeePassXC importable CSV files.

Usage:

```
python psafe3-to-keepass-csv.py ./secret.psafe3 ./exported.csv
```

It will prompt for the password.

Then in KeePassXC choose "Database" > "Import" > "CSV File" then map the fields to the corresponding CSV columns.
