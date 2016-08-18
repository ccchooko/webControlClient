# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(
    version="0.0.1",
    description="WEB CONTROL CLIENT",
    name="webControlClient",

    console=["wcc.py"],
    data_files=[("config.ini"),],
)
