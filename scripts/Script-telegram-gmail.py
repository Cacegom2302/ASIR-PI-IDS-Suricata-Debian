#!/usr/bin/env python3

import subprocess
import requests
import smtplib
import time
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ── CONFIGURACIÓN ──────────────────────────────────────────
TELEGRAM_TOKEN  = "8240407473:AAH-xOWfBMu1t6ZNyk9HfW1yq59kL-1G5AE"
TELEGRAM_CHAT_ID = "1476121883"

EMAIL_ORIGEN  = "caesaracevedo03@gmail.com"
EMAIL_DESTINO = "caesaracevedo03@gmail.com"
EMAIL_PASSWORD = "xslw pwlm udah bxsk"

LOG_SURICATA = "/var/log/suricata/fast.log"
# ───────────────────────────────────────────────────────────

alertas_enviadas = set()

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": mensaje})
    except Exception as e:
        print(f"[ERROR Telegram] {e}")

def enviar_email(asunto, cuerpo):
    try:
        msg = MIMEMultipart()
        msg["From"]    = EMAIL_ORIGEN
        msg["To"]      = EMAIL_DESTINO
        msg["Subject"] = asunto
        msg.attach(MIMEText(cuerpo, "plain"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ORIGEN, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ORIGEN, EMAIL_DESTINO, msg.as_string())
    except Exception as e:
        print(f"[ERROR Email] {e}")

##────La alerta del correo , y el telegram ──────────────────────────────────────────────
def monitorear():
    print("[*] Monitoreando Suricata - alertas activas...")
    with open(LOG_SURICATA, "r") as f:
        f.seek(0, 2)  # ir al final del fichero
        while True:
            linea = f.readline()
            if not linea:
                time.sleep(1)
                continue
            linea = linea.strip()
            if linea and linea not in alertas_enviadas:
                alertas_enviadas.add(linea)
                print(f"[ALERTA] {linea}")
                mensaje = f"🚨 ALERTA IDS SURICATA\n\n{linea}"
                enviar_telegram(mensaje)
                enviar_email("🚨 Alerta IDS Suricata", linea)

if __name__ == "__main__":
    monitorear()

