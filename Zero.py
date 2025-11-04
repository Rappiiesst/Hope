#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sanitized demo of the provided script:
- Paid-key check removed
- Harmful network/brute-force code removed or replaced with safe stubs
- Big ASCII "ROHIT" banner inserted
- Menus, UID generation, and worker threading preserved for demo/testing
"""

import os
import sys
import random
import string
import time
import uuid
from concurrent.futures import ThreadPoolExecutor as tred
from random import randint as rr

# Try to not auto-install anything; just keep imports minimal and safe.
# Terminal title (stylish)
try:
    sys.stdout.write('\x1b]2;𓆩★ROHIT★𓆪 \x07')
except Exception:
    pass

# Color codes
GREEN = "\033[1;32m"
RESET = "\033[0m"

# Globals
method = []
oks = []
cps = []
loop = 0
user = []

def clear_screen():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')

def linex():
    print('\x1b[38;5;48m' + "━" * 54)

def windows():
    """
    Generates a random Windows User-Agent string (harmless generator).
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000,7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0','1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000,7000))}.{random.choice(range(50,200))} Safari/{bz}"
    C = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{random.choice(range(1,7120))}.0 Safari/537.36"
    return random.choice([A, B, C])

def window1():
    """
    Another variant for demo user-agent.
    """
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0','11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([D])

# Set window title for terminals that support it
try:
    sys.stdout.write('\x1b]2;𓆩【 ROHIT KING】𓆪 \x07')
except Exception:
    pass

# -------------------------
# Banner with ROHIT (Inserted)
# -------------------------
def ____banner____():
    clear_screen()
    # Big ASCII "ROHIT" logo
    print("\033[1;32m")
    print("  ██████╗  ██████╗  ██╗  ██╗ ██╗ ██████╗ ███████╗")
    print(" ██╔═══██╗██╔═══██╗ ██║ ██╔╝ ██║██╔═══██╗╚══███╔╝")
    print(" ██║   ██║██║   ██║ █████╔╝  ██║██║   ██║  ███╔╝ ")
    print(" ██║   ██║██║   ██║ ██╔═██╗  ██║██║   ██║ ███╔╝  ")
    print(" ╚██████╔╝╚██████╔╝ ██║  ██╗ ██║╚██████╔╝███████╗")
    print("  ╚═════╝  ╚═════╝  ╚═╝  ╚═╝ ╚═╝ ╚═════╝ ╚══════╝")
    print()
    print("             𓆩★  R O H I T  ★𓆪")
    print("         — Safe Demo / Sanitized Script —")
    print("\033[0m")
    linex()

# -------------------------
# Utility: estimate creation year (kept from original; harmless)
# -------------------------
def creationyear(uid):
    """
    Estimate a year based on UID-like string patterns.
    This is purely heuristic and for demo/UX only.
    """
    s = str(uid)
    if len(s) == 15:
        if s.startswith('1000000000'):
            return '2009'
        if s.startswith('100000000'):
            return '2009'
        if s.startswith('10000000'):
            return '2009'
        if s.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if s.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if s.startswith('100001'):
            return '2010'
        if s.startswith(('100002', '100003')):
            return '2011'
        if s.startswith('100004'):
            return '2012'
        if s.startswith(('100005', '100006')):
            return '2013'
        if s.startswith(('100007', '100008')):
            return '2014'
        if s.startswith('100009'):
            return '2015'
        if s.startswith('10001'):
            return '2016'
        if s.startswith('10002'):
            return '2017'
        if s.startswith('10003'):
            return '2018'
        if s.startswith('10004'):
            return '2019'
        if s.startswith('10005'):
            return '2020'
        if s.startswith('10006'):
            return '2021'
        if s.startswith('10009'):
            return '2023'
        if s.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(s) in (9, 10):
        return '2008'
    elif len(s) == 8:
        return '2007'
    elif len(s) == 7:
        return '2006'
    elif len(s) == 14 and s.startswith('61'):
        return '2024'
    else:
        return ''

# -------------------------
# Menus and flows (sanitized)
# -------------------------
def BNG_71_():
    ____banner____()
    print('       (A) > × < OLD CLONE (demo)')
    linex()
    __Jihad__ = input("       (★) > × < CHOICE (A): ").strip().upper()
    if __Jihad__ in ('A', 'a', '01', '1', ''):
        old_clone()
    else:
        print("\n    Choose Valid Option...")
        time.sleep(1)
        BNG_71_()

def old_clone():
    """
    Demo menu for 'old clone' area.
    Instead of harmful actions, it simulates ID generation and runs safe tasks.
    """
    global user
    user = []
    ____banner____()
    print("       (★) > × < Old Code Demo")
    linex()
    ask = input("       (★) > × < SELECT (type 1 for sample behavior): ").strip()
    linex()
    ____banner____()
    print("       (★) > × < EXAMPLE COUNT: 20000 / 30000 / 99999")
    limit = input("       (★) > × < ENTER COUNT (e.g. 50): ").strip()
    if not limit.isdigit() or int(limit) <= 0:
        print("Invalid number. Using default 50.")
        limit = "50"
    limit = int(limit)
    # simulate generation of ids (non-sensitive)
    for _ in range(limit):
        # create 10-digit demo ids
        data = ''.join(random.choices('0123456789', k=10))
        user.append(data)

    print('       (A) > × < METHOD 1 (demo)')
    print('       (B) > × < METHOD 2 (demo)')
    linex()
    meth = input("       (★) > × < CHOICE (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       (★) > × < TOTAL IDS: {limit}")
        print("       (★) > × < USE AIRPLANE MODE FOR BETTER NETWORK (demo note)")
        linex()
        for mal in user:
            if meth == 'A':
                pool.submit(login_stub, mal, method='M1')
            elif meth == 'B':
                pool.submit(login_stub, mal, method='M2')
            else:
                # default safe action
                pool.submit(dummy_work, mal)

def old_Tow():
    """
    Another demo branch kept for structure parity with original.
    """
    user = []
    ____banner____()
    limit = input("       (★) > × < ENTER COUNT (e.g. 30): ").strip()
    if not limit.isdigit() or int(limit) <= 0:
        limit = "30"
    limit = int(limit)
    prefixes = ['100003', '100004']
    for _ in range(limit):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('       (A) > × < METHOD A (demo)')
    print('       (B) > × < METHOD B (demo)')
    meth = input("       (★) > × < CHOICE (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       (★) > × < TOTAL IDS: {limit}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_stub, uid, method='A')
            elif meth == 'B':
                pool.submit(login_stub, uid, method='B')
            else:
                pool.submit(dummy_work, uid)

def old_Tree():
    """
    Third demo branch (keeps parity with original).
    """
    user = []
    ____banner____()
    limit = input("       (★) > × < ENTER COUNT (e.g. 30): ").strip()
    if not limit.isdigit() or int(limit) <= 0:
        limit = "30"
    limit = int(limit)
    prefix = '1000004'
    for _ in range(limit):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('       (A) > × < METHOD A (demo)')
    print('       (B) > × < METHOD B (demo)')
    meth = input("       (★) > × < CHOICE (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       (★) > × < TOTAL IDS: {limit}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_stub, uid, method='A')
            elif meth == 'B':
                pool.submit(login_stub, uid, method='B')
            else:
                pool.submit(dummy_work, uid)

# -------------------------
# Safe stubs and dummy workers
# -------------------------
def dummy_work(uid):
    """
    Safe placeholder function that simulates processing (no external calls).
    """
    global loop
    time.sleep(0.05 + random.random() * 0.2)
    loop += 1
    sys.stdout.write(f"\rProcessed (demo) UID {uid}  |  total: {loop}")
    sys.stdout.flush()

def login_stub(uid, method=None):
    """
    Replaces original login/brute-force attempts.
    This stub simulates results for demo only.
    - Randomly marks some UIDs as 'ok' or 'checkpoint' purely for demonstration.
    """
    global loop, oks, cps
    time.sleep(0.05 + random.random() * 0.15)
    # simulate a small chance of "ok" or "checkpoint"
    r = random.random()
    if r < 0.005:
        oks.append(uid)
        # safe local logging (non-sensitive)
        try:
            open('ROHIT_OK_DEMO.txt', 'a').write(f"{uid}|demo_pass\n")
        except Exception:
            pass
        status = "OK"
    elif r < 0.02:
        cps.append(uid)
        try:
            open('ROHIT_CP_DEMO.txt', 'a').write(f"{uid}|demo_checkpoint\n")
        except Exception:
            pass
        status = "CP"
    else:
        status = "FAIL"
    loop += 1
    sys.stdout.write(f"\r[{method or 'M'}] UID {uid} → {status}  |  processed: {loop}")
    sys.stdout.flush()

# -------------------------
# Security class (non-invasive)
# -------------------------
class sec:
    """
    Non-invasive placeholder security class.
    Original code had file-system checks; we avoid doing destructive checks.
    This placeholder simply exists so the original script structure is preserved.
    """
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
    def linex(self):
        linex()

# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    try:
        BNG_71_()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
