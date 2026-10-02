# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T02:30:42.125349+00:00
État : OK | marchés EUR : 430 | V4 : 386 | données valides : 430
Récupération : 2026-10-02T02:30:15.422111+00:00 | âge ticker : 151.1 s | durée : 152.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- HBAR-EUR : 0.091807 € ; score 88.65/100 ; SURVEILLE ; seuil achat non atteint
- ICP-EUR : 2.9402 € ; score 88.57/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BABY-EUR : 0.012226 € ; score 87.71/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- NEAR-EUR : 4.3915 € ; score 86.97/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.43944 € ; score 86.95/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00061582 | +138.80 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.149108 | +79.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 2.5238 | +25.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SCR-EUR | 0.027599 | +25.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04753 | +23.45 % | DETECTED_EARLY | NONE | NONE |
| SYN-EUR | 0.16638 | +19.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.43467 | +19.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.002449 | +18.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.20772 | +17.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALICE-EUR | 0.1731 | +17.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1949 scans ; 834148 observations ; 1515 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
