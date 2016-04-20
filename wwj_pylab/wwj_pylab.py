#!/usr/bin/env python
# encoding: utf-8

import requests
import click
from ConfigParser import SafeConfigParser
import sys
#debug mode :log

class PyLab(object):
    """
    my python laboratory
    """
    def __init__(self,lab_name="Mend the Sky"):
        self.lab_name = lab_name
    def py_patch_hello(self,code_url):
        """
        inspired by JSPatch
        """
        #get code
        code_url = "http://7fvio7.com1.z0.glb.clouddn.com/online_code.py"
        r = requests.get(code_url)
        if r.status_code == 200:
            r_content = r.content
            code_str = r_content
        try:
            exec(code_str, globals()) #get hello function
            print hello() #OK!
        except:
            raise

    def py_patch(self,code_url):
        """
        inspired by JSPatch
        """
        #get code
        r = requests.get(code_url)
        if r.status_code == 200:
            r_content = r.content
            code_str = r_content
        try:
            exec(code_str, globals()) #get hello function
            print cloud_code() #http://7fvio7.com1.z0.glb.clouddn.com/cloud_code.py
        except:
            raise


@click.command()
@click.option('--code_url',default="http://7fvio7.com1.z0.glb.clouddn.com/cloud_code.py", help='The url of  cloud python code.')
def main(code_url):
    #正则判断url有误？
    if not code_url:
        click.echo("require --code_url url")
        sys.exit(0)
    mylab = PyLab()
    mylab.py_patch(code_url)

if __name__ == '__main__':
    main()
