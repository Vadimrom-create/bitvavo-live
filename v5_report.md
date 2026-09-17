# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-17T06:00:42.635618+00:00
État : OK | marchés EUR : 430 | V4 : 376 | données valides : 2
Récupération : 2026-09-17T06:00:11.910559+00:00 | âge ticker : 148.0 s | durée : 148.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 21/430 ; 15 min 41/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PORTAL-EUR : WICK_SETUP, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- XPL-EUR : INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- LSK-EUR : 0.44209 € ; score 76.34/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.154787 | +58.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVA-EUR | 0.21219 | +57.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.057304 | +25.92 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| HNT-EUR | 0.41742 | +22.17 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| USELESS-EUR | 0.232252 | +20.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HEI-EUR | 0.117302 | +20.52 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| QUID-EUR | 0.059603 | +20.39 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| VVV-EUR | 21.739 | +15.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.023465 | +13.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LIGHTER-EUR | 4.1541 | +13.80 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 690 scans ; 296094 observations ; 117 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
