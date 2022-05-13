from ast import arguments
from pydoc import describe
import password as pw
import description as programDescription
import argparse


parser = argparse.ArgumentParser(
    prog='pwmanager',
    exit_on_error=True,
    description=programDescription.program_description
)
print(parser.description)
parser.add_argument('-n', help='Number of characters to add. default is 8 and max is 32',
                    type=int, default=8, required=False)
args = parser.parse_args()

if args.n is None:
    pw_create = pw.Password()
    password = pw_create.create_password(8)
    print(password)
elif args.n < 8:
    print('At least 8 characters needed')
elif args.n > 32:
    print('At least 8 characters needed')
else:
    pw_create = pw.Password()
    password = pw_create.create_password(args.n)
    print(password)
