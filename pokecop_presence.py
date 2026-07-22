import time
from pypresence import Presence

# ---- CONFIG ----
CLIENT_ID = "1529255408554741960"
DETAILS = "🚀 Prépare la mise à jour du plus grand serveur ACO FR-BE !"
STATE = ""  # laisse vide pour ne PAS dupliquer une ligne en dessous
LARGE_IMAGE_KEY = "soon"
LARGE_IMAGE_TEXT = "KOOP ACO"
SMALL_IMAGE_KEY = "nath"
SMALL_IMAGE_TEXT = "nathbrt"
SERV_LINK = "https://discord.gg/mvUyhnwNk"
BUTTON_LABEL = "Rejoins nous"
UPDATE_INTERVAL_SECONDS = 15  # Discord coupe la presence si pas de refresh régulier


def connect():
    while True:
        try:
            rpc = Presence(CLIENT_ID)
            rpc.connect()
            print("Connecte a Discord RPC. Presence active. Ctrl+C pour arreter.")
            return rpc
        except Exception as e:
            print(f"Discord pas encore lance ou injoignable ({e}), nouvel essai dans 10s...")
            time.sleep(10)


def run():
    rpc = connect()
    start_time = time.time()
    while True:
        try:
            rpc.update(
                details=DETAILS,
                state=STATE if STATE else None,
                large_image=LARGE_IMAGE_KEY,
                large_text=LARGE_IMAGE_TEXT,
                small_image=SMALL_IMAGE_KEY,
                small_text=SMALL_IMAGE_TEXT,
                start=start_time,
                buttons=[{"label": BUTTON_LABEL, "url": SERV_LINK}],
            )
        except Exception as e:
            print(f"Erreur update, reconnexion... ({e})")
            rpc = connect()
        time.sleep(UPDATE_INTERVAL_SECONDS)


if __name__ == "__main__":
    run()
