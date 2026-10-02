# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T06:54:32.702137+00:00
État : OK | marchés EUR : 430 | V4 : 385 | données valides : 430
Récupération : 2026-10-02T06:53:56.266550+00:00 | âge ticker : 157.2 s | durée : 157.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WLD-EUR : 0.4768 € ; score 90.26/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.113099 € ; score 87.45/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GRT-EUR : 0.025801 € ; score 82.70/100 ; SURVEILLE ; seuil achat non atteint
- RUNE-EUR : 0.70464 € ; score 82.41/100 ; SURVEILLE ; seuil achat non atteint
- MON-EUR : 0.030357 € ; score 82.29/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.0007381 | +183.99 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.130074 | +51.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.47883 | +29.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SCR-EUR | 0.027588 | +21.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.20355 | +12.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.7115 | +12.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.84 | +12.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04556 | +12.11 % | DETECTED_EARLY | NONE | NONE |
| AAVE-EUR | 164.39 | +10.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.159084 | +10.01 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1962 scans ; 839738 observations ; 1534 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
