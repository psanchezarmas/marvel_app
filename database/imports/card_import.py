import json
import os

import requests
from dotenv import load_dotenv
from supabase import Client, create_client

# === 1. Load credentials from .env.local ===
load_dotenv(".env.local")
url = os.getenv("NEXT_PUBLIC_SUPABASE_URL")
key = os.getenv("NEXT_PUBLIC_SUPABASE_ANON_KEY")

supabase: Client = create_client(url, key)

# === 2. Fetch MarvelCDB cards ===
response = requests.get("https://marvelcdb.com/api/public/cards")
cards = response.json()

# === 3. Insert into Supabase (assumes 'cards' table exists and matches schema) ===
for card in cards:
    data = {
        "code": card.get("code"),
        "name": card.get("name"),
        "real_name": card.get("real_name"),
        "subname": card.get("subname"),
        "pack_code": card.get("pack_code"),
        "pack_name": card.get("pack_name"),
        "type_code": card.get("type_code"),
        "type_name": card.get("type_name"),
        "faction_code": card.get("faction_code"),
        "faction_name": card.get("faction_name"),
        "position": card.get("position"),
        "cost": card.get("cost"),
        "cost_per_hero": card.get("cost_per_hero"),
        "text": card.get("text"),
        "real_text": card.get("real_text"),
        "quantity": card.get("quantity"),
        "resource_energy": card.get("resource_energy"),
        "health": card.get("health"),
        "health_per_hero": card.get("health_per_hero"),
        "attack": card.get("attack"),
        "attack_cost": card.get("attack_cost"),
        "base_threat_fixed": card.get("base_threat_fixed"),
        "escalation_threat_fixed": card.get("escalation_threat_fixed"),
        "threat_fixed": card.get("threat_fixed"),
        "deck_limit": card.get("deck_limit"),
        "traits": card.get("traits"),
        "real_traits": card.get("real_traits"),
        "is_unique": card.get("is_unique"),
        "hidden": card.get("hidden"),
        "permanent": card.get("permanent"),
        "double_sided": card.get("double_sided"),
        "octgn_id": card.get("octgn_id"),
        "attack_star": card.get("attack_star"),
        "thwart_star": card.get("thwart_star"),
        "defense_star": card.get("defense_star"),
        "health_star": card.get("health_star"),
        "recover_star": card.get("recover_star"),
        "scheme_star": card.get("scheme_star"),
        "boost_star": card.get("boost_star"),
        "threat_star": card.get("threat_star"),
        "escalation_threat_star": card.get("escalation_threat_star"),
        "url": card.get("url"),
        "image_url": f"https://marvelcdb.com{card['imagesrc']}" if card.get("imagesrc") else None,
        "raw_data": card
    }

    supabase.table("cards").upsert(data).execute()

print("✅ All cards synced via Supabase client.")
