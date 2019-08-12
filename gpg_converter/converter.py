#!/bin/python

import click
import subprocess, glob
from jinja2 import Template

csv_format=Template("{{url}},,{{username}},{{password}},,{{extra}},{{name}},")


def convert_helper(src, dst, name, passphrase):
    url, username, password, extra = "", "", "", ""
    try:
        fname = name + ".csv"
        subprocess.run(["gpg2", "--passphrase", passphrase, "--batch", "--output",
                        fname, "--decrypt", src])

        with open(fname, 'r') as r, open(dst, 'a') as w:
            for line in r:
                x=0
                line_s = line.split("login:")
                if line_s[0] == "":
                    username = line_s[-1].strip()
                    x+=1
                line_s = line.split("url:")
                if line_s[0] == "":
                    url = line_s[-1].strip()
                    x+=1
                line_s = line.split("other:")
                if line_s[0] == "":
                    extra = line_s[-1].strip()
                    x+=1
                if x == 0:
                    password = line.strip()

            text = csv_format.render(url=url, username=username, password=password, extra=extra, name=name.split("/")[-1])
            w.write(text+"\n")

        subprocess.run(["rm", "-rf", fname])

    except:
        print("An exception occurred..")


@click.group()
def converter():
    pass

@converter.command()
@click.option('--src', help='Source GPG file.')
@click.option('--dst', help='Destination filename')
@click.option('--passphrase',prompt='Your passphrase: ', hide_input=True, confirmation_prompt=True)
def convert(src, dst, passphrase):
    """This converts a src GPG file to a dst CSV file."""
    with open(dst, 'w') as w:
        w.write("url,type,username,password,hostname,extra,name,grouping\n")
    name = src.split(".gpg")[0]
    convert_helper(src, dst, name, passphrase)

@converter.command()
@click.option('--src', help='Source GPG directory.')
@click.option('--dst', help='Destination filename')
@click.option('--passphrase', prompt='Your passphrase: ', hide_input=True, confirmation_prompt=True)
def convertdir(src, dst, passphrase):
    """This converts all GPG files in a dir to a single CSV file."""
    with open(dst, 'w') as w:
        w.write("url,type,username,password,hostname,extra,name,grouping\n")

    glob_pattern = src + "*.gpg"
    for f in glob.glob(glob_pattern):
        name = f.split(".gpg")[0]
        convert_helper(f, dst, name, passphrase)

if __name__ == '__main__':
    converter()
