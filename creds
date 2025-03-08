#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Search for default credentials using the DefaultCreds-cheat-sheet database.
code structure inspired by @ncrocfer whatportis project.
'''
__author__ = "ihebski"
__version__ = "0.5.3"
__codename__ = 'creds'
__source__ ="https://github.com/ihebski/DefaultCreds-cheat-sheet"

from tinydb import TinyDB,Query,where
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware
from prettytable import PrettyTable
from urllib3.exceptions import InsecureRequestWarning
import urllib3
from pathlib import Path
import csv
import requests
import fire
import pathlib
import hashlib
import tempfile

urllib3.disable_warnings(InsecureRequestWarning)

tmpdir = tempfile.gettempdir()
path = pathlib.Path(__file__).parent
db = TinyDB(f"{path}/DefaultCreds_db.json",storage=CachingMiddleware(JSONStorage))
DefaultCreds_CSV_FILE = "https://raw.githubusercontent.com/ihebski/DefaultCreds-cheat-sheet/main/DefaultCreds-Cheat-Sheet.csv"

def get_db(path=path,msg="[+] Download database...",proxy=None):
    """
    This function downloads the DefaultCreds-Cheat-Sheet.csv file and converted into a json database.
    https://tinydb.readthedocs.io/en/latest/usage.html
    """
    try:
        db = TinyDB(f"{path}/DefaultCreds_db.json",storage=CachingMiddleware(JSONStorage))
        vendor = []
        proxies = {'http': proxy, 'https': proxy} if proxy else None
        r = requests.get(DefaultCreds_CSV_FILE,proxies=proxies,verify=False).content.decode("utf-8")
        print(msg)
        data = csv.reader(r.splitlines())
        for row in data:
            vendor.append(
                {
                    "product" : row[0].lower().strip() if row[0] else "-",
                    "username" : row[1].strip() if row[0] else "-",
                    "password" : row[2].strip() if row[0] else "-"
                }
            )
        db.truncate()
        db.insert_multiple(vendor)
        db.close()
    except Exception as e:
        print(f"An error occurred: {e}")

def export_creds(product,keyword):
    """
    Export usernames and passwords to separated files
    :param list(dict(product))
    :param keyword
    :return 2 files
    """
    # username and passwords default files paths
    username_path = f"{tmpdir}/{keyword}-usernames.txt"
    passwords_path = f"{tmpdir}/{keyword}-passwords.txt"

    # Create lists for (usernames,passwords) and remove duplicates
    username_list, password_list = set([row.get("username").replace('<blank>','') for row in product]), set([row.get("password").replace('<blank>','') for row in product])
    
    # Create files if not exist
    if not all([Path(username_path).is_file(),Path(passwords_path).is_file()]):
        with open(f'{username_path}', "w") as outfile_usernames, open(f'{passwords_path}', "w") as outfile_passwords:
            outfile_usernames.write("\n".join(username_list))
            outfile_passwords.write("\n".join(password_list))
        print(f"\n[+] Creds saved to {username_path} , {passwords_path} 📥")
    else:
        print(f"\n[!] Creds already exists under {username_path} , {passwords_path} ⛔️")

def print_table(product,keyword,export):
    """
    This function returns a pretty table used to display the results.
    :param list of searched products
    https://pypi.org/project/prettytable/
    """
    if len(product) == 0:
        print("[-] Product not found in database 🦕")
    else:
        table = PrettyTable(["Product", "username", "password"])
        table.align["Product"] = "l"
        table.padding_width = 1
        for row in product:
            table.add_row([row.get("product"),row.get("username"),row.get("password")])
        print(table)
        if export: export_creds(product,keyword)

def search(keyword,export=False,proxy=None):
    """
    This function search for a product using like statement
    :param keyword
    :return table
    """
    if not db.all() :
        get_db(proxy=proxy)
        print_table(db.search(where("product").search(str(keyword).lower())),keyword,export)
    else:
        print_table(db.search(where("product").search(str(keyword).lower())),keyword,export)

def sha256sum(filename):    
    """
    This function is used to compare two file hashes
    :param filename path
    :return sha256sum hash
    """
    hash_sha256 = hashlib.sha256()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def update(proxy=None):
    """
    Update database records
    """
    try:
        get_db(tmpdir,"Check for new updates...🔍",proxy)
        print('[+] No action needed, We are fine 🤘') if sha256sum(f'{tmpdir}/DefaultCreds_db.json') == sha256sum(f"{path}/DefaultCreds_db.json") else get_db(path,"New updates are available 🚧\n[+] Download database...",proxy)
    except Exception as e:
        print("⚠️ Operation failed, An error occurred while updating records !! 🦄 {e}")

def version():
    print(f"[INF] DefaultCreds-cheat-sheet Version: v{__version__}")

def run():
    fire.Fire()

if __name__ == "__main__":
    run()
