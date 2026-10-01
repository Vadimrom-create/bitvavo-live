# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T13:52:08.775146+00:00
État : OK | marchés EUR : 430 | V4 : 384 | données valides : 430
Récupération : 2026-10-01T13:51:35.206101+00:00 | âge ticker : 149.3 s | durée : 150.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- TRB-EUR : 19.088 € ; score 90.74/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SYRUP-EUR : 0.20417 € ; score 88.17/100 ; SURVEILLE ; seuil achat non atteint
- RED-EUR : 0.16169 € ; score 85.53/100 ; SURVEILLE ; SPREAD_RISK
- AAVE-EUR : 145.29 € ; score 84.20/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.093379 € ; score 82.73/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00062728 | +142.32 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.4481 | +77.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.44537 | +43.36 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CAP-EUR | 0.0692503 | +24.15 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MON-EUR | 0.028745 | +16.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.33136 | +15.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VELO-EUR | 0.0052074 | +14.58 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| HEI-EUR | 0.139146 | +13.86 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SYN-EUR | 0.167 | +13.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.002429 | +13.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1911 scans ; 817808 observations ; 1478 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
