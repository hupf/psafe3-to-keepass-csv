import sys
import csv
from datetime import datetime
from argparse import ArgumentParser
from getpass import getpass
from loxodo.vault import Vault

class HelpfulArgumentParser(ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

parser = HelpfulArgumentParser(description='Convert a Password Safe v3 file to a CSV file (cleartext!) that can be imported with KeePassXC.')
parser.add_argument('input_file', help='Input file in Password Safe v3 format')
parser.add_argument('output_file', help='Output file in unencrypted (!) CSV format')

args = parser.parse_args()
input_file = args.input_file
output_file = args.output_file

password = getpass()

vault = Vault(password, input_file)

with open(output_file, 'wb') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['group', 'title', 'username', 'password', 'url', 'notes', 'modified'])

    for record in vault.records:
        writer.writerow([
            # group
            record._get_group().encode('utf-8'),

            # title
            record._get_title().encode('utf-8'),

            # username
            record._get_user().encode('utf-8'),

            # password
            record._get_passwd().encode('utf-8'),

            # url
            record._get_url(),

            # notes
            record._get_notes().encode('utf-8'),

            # last mofified
            datetime.fromtimestamp(record.last_mod).isoformat()
        ])
