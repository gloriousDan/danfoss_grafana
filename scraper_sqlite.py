import pandas
from datetime import datetime
from ftplib import FTP
from sqlalchemy import create_engine, text , inspect
from io import BytesIO
from os import environ

DB_FILE_NAME = environ.get("DB_FILE_NAME")
DB_TABLE_NAME = environ.get("DB_TABLE_NAME")

FTP_LOGIN = environ.get("FTP_LOGIN") 
FTP_PASS = environ.get("FTP_PASS") 
FTP_DIR = environ.get("FTP_DIR")
FTP_URL = environ.get("FTP_URL")

def get_and_convert_dataframe(buffer):
    # pandas
    df = pandas.read_csv(buffer, sep=";", skiprows=5, skipfooter=1, engine="python")
    df["TIMESTAMP"] = df["TIMESTAMP"].map(lambda x: datetime.fromisoformat(x).timestamp())
    return df


def get_scanned_files(engine):
    with engine.connect() as conn:
        insp = inspect(engine)
        if insp.has_table(DB_TABLE_NAME):
            result = conn.execute(text(f"select distinct source_file from '{DB_TABLE_NAME}'"))
            return {entry[0] for entry in result.all()}
        else:
            return {}



engine = create_engine(f"sqlite:///db/{DB_FILE_NAME}")


already_imported_files = get_scanned_files(engine)

df = None

ftp = FTP(FTP_URL)
ftp.login(FTP_LOGIN, FTP_PASS)
ftp.cwd(FTP_DIR)
files = []
ftp.retrlines("NLST", lambda f: files.append(f))

for file in (file for file in files if file not in already_imported_files):
    try:
        with BytesIO() as buf:
            # download file from ftp and save it to a buffer
            ftp.retrbinary(f"RETR {file}", buf.write)
            buf.seek(0)

            # parse file and get df from buffer
            new_df = get_and_convert_dataframe(buf)

            new_df["source_file"] = file
            if df is not None:
                df = pandas.concat([df, new_df])
            else: 
                df = new_df
    except FileNotFoundError as e:
        print(f"Warning: File not Found: {e}") 

if df is not None:
    df = df.set_index("TIMESTAMP")

    df.to_sql(DB_TABLE_NAME, con=engine, if_exists="append")
else:
    print(f"No new files added to db")


