from os.path import exists; from ctypes import windll; from subprocess import run, CREATE_NO_WINDOW; from urllib.request import urlopen, Request; from json import dumps; from random import choices; from string import ascii_letters, digits; P = "C:\\Program Files\\Cloudflare\\Cloudflare WARP"; [windll.user32.MessageBoxW(0, "Cloudflare Warp is not Installed", "Error", 0), exit()] if not exists(P) else None; o = run([f"{P}/warp-cli.exe", "registration", "show"], capture_output=True, text=True, creationflags=CREATE_NO_WINDOW).stdout.split("\n"); s = urlopen(Request('https://api.cloudflareclient.com/v0a{}/reg'.format("".join(choices(digits, k=3))), dumps({"key": "{}=".format(''.join(choices(ascii_letters + digits, k=43))), "referrer": o[1].split(":")[1].strip()}).encode('utf8'), headers={'Host': 'api.cloudflareclient.com', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.12.1'})).getcode(); run([f"{P}/warp-cli.exe", "set-license", o[4].split(":")[1].strip()], capture_output=True, text=True, creationflags=CREATE_NO_WINDOW); windll.user32.MessageBoxW(0, "Successfully Registered" if s == 200 else "Failed to Register", "Activated by IRedDragonICY" if s == 200 else "Error", 0)