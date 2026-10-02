# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T10:57:49.681744+00:00
État : OK | marchés EUR : 430 | V4 : 392 | données valides : 430
Récupération : 2026-10-02T10:57:16.409760+00:00 | âge ticker : 154.0 s | durée : 155.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- NOM-EUR : 0.002243 € ; score 93.45/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- SHIB-EUR : 5.2425e-06 € ; score 86.22/100 ; SURVEILLE ; seuil achat non atteint
- PORTAL-EUR : 0.015955 € ; score 84.19/100 ; SURVEILLE ; seuil achat non atteint
- PARTI-EUR : 0.024832 € ; score 83.85/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SOLV-EUR : 0.0038276 € ; score 83.23/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00071787 | +63.15 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SAND-EUR | 0.059206 | +56.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.11861 | +33.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.53554 | +26.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.093859 | +19.72 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SCR-EUR | 0.026515 | +18.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MAGIC-EUR | 0.054048 | +15.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.6532 | +14.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZK-EUR | 0.012074 | +14.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.20079 | +13.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1974 scans ; 844898 observations ; 1557 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
