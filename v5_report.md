# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T00:55:14.356184+00:00
État : OK | marchés EUR : 430 | V4 : 384 | données valides : 430
Récupération : 2026-10-02T00:54:14.462748+00:00 | âge ticker : 177.4 s | durée : 178.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- RARE-EUR : 0.015639 € ; score 88.34/100 ; SURVEILLE ; WICK_SETUP
- LTC-EUR : 61.407 € ; score 87.76/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- STRK-EUR : 0.037828 € ; score 87.31/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 105.727 € ; score 86.84/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : 0.11222 € ; score 86.35/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00053292 | +106.65 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.132774 | +59.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 2.7035 | +34.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.19449 | +30.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MEGA-EUR | 0.04756 | +27.40 % | DETECTED_EARLY | NONE | NONE |
| CT-EUR | 0.44083 | +23.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0025087 | +19.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.16423 | +17.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.2048 | +15.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| VELO-EUR | 0.0054057 | +14.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1944 scans ; 831998 observations ; 1513 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
