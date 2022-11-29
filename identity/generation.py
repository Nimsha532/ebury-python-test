# -*- coding: utf-8 -*-

from .constants import ID_CHARACTERS
import secrets
N=7
def generate():
    return ''.join(secrets.choice(ID_CHARACTERS) for _ in range(N))

