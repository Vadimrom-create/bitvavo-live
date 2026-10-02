# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T01:34:56.224748+00:00
État : OK | marchés EUR : 430 | V4 : 385 | données valides : 430
Récupération : 2026-10-02T01:34:22.327195+00:00 | âge ticker : 156.7 s | durée : 158.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- RARE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZRO-EUR : 1.6397 € ; score 92.84/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : 0.11506 € ; score 87.04/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : 0.049837 € ; score 86.85/100 ; SURVEILLE ; WICK_SETUP
- SPK-EUR : 0.021166 € ; score 85.75/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- DYDX-EUR : 0.13271 € ; score 84.89/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00051303 | +98.94 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.1571 | +90.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 2.6004 | +32.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04742 | +24.46 % | DETECTED_EARLY | NONE | NONE |
| SCR-EUR | 0.026137 | +22.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.17579 | +18.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.165088 | +18.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0024593 | +17.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.418 | +14.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.19938 | +13.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1946 scans ; 832858 observations ; 1513 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
