# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T02:10:42.823194+00:00
État : OK | marchés EUR : 430 | V4 : 386 | données valides : 430
Récupération : 2026-10-02T02:10:13.669648+00:00 | âge ticker : 148.5 s | durée : 149.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- BTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZRO-EUR : 1.6312 € ; score 93.44/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.20959 € ; score 88.84/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- IMX-EUR : 0.15567 € ; score 88.52/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- ICP-EUR : 2.9357 € ; score 87.98/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.110462 € ; score 87.88/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00066285 | +157.04 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.146152 | +76.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SCR-EUR | 0.029358 | +36.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVR-EUR | 2.5567 | +24.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04786 | +23.86 % | DETECTED_EARLY | NONE | NONE |
| NOM-EUR | 0.0025018 | +22.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.165537 | +20.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.1742 | +18.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.422 | +16.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.20394 | +15.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1948 scans ; 833718 observations ; 1514 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
