# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T10:40:16.441926+00:00
État : OK | marchés EUR : 430 | V4 : 390 | données valides : 430
Récupération : 2026-10-02T10:39:43.615479+00:00 | âge ticker : 152.1 s | durée : 152.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- HBAR-EUR : 0.094448 € ; score 92.84/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : 9.9461 € ; score 86.92/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : 0.07956 € ; score 85.22/100 ; SURVEILLE ; LOW_LIQUIDITY
- XPL-EUR : 0.088414 € ; score 84.67/100 ; SURVEILLE ; WICK_SETUP
- CC-EUR : 0.10867 € ; score 84.57/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00071332 | +142.88 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SAND-EUR | 0.056565 | +48.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.120672 | +33.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SCR-EUR | 0.027357 | +22.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.52984 | +17.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.20655 | +17.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MANA-EUR | 0.091394 | +16.52 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MAGIC-EUR | 0.053624 | +15.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SKY-EUR | 0.080125 | +14.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZK-EUR | 0.012059 | +13.99 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1973 scans ; 844468 observations ; 1557 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
