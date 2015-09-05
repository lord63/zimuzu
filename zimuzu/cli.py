#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import click

from zimuzu import __version__
from zimuzu.zumuzu_tv import Zimuzu


@click.group(context_settings={'help_option_names': ('-h', '--help')})
@click.version_option(__version__, '-V', '--version', message='%(version)s')
def cli():
    """Do sign for ZIMUZU: http://www.zimuzu.tv/."""
    pass


@cli.command()
def sign():
    """Do the sign."""
    zimuzu = Zimuzu()
    zimuzu.login()
    zimuzu.do_sign()
