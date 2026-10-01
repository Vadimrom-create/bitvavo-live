# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T21:41:00.385051+00:00
État : OK | marchés EUR : 430 | V4 : 379 | données valides : 430
Récupération : 2026-10-01T21:40:27.002309+00:00 | âge ticker : 156.1 s | durée : 157.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JASMY-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- DYDX-EUR : 0.13315 € ; score 93.29/100 ; SURVEILLE ; seuil achat non atteint
- JASMY-EUR : 0.0050217 € ; score 91.81/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- XYO-EUR : 0.0033693 € ; score 88.80/100 ; SURVEILLE ; LOW_LIQUIDITY
- GRAM-EUR : 1.3919 € ; score 86.43/100 ; SURVEILLE ; WICK_SETUP
- AAVE-EUR : 151.04 € ; score 82.85/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00068093 | +167.32 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.13185 | +59.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALICE-EUR | 0.20176 | +36.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 2.5069 | +31.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.43662 | +26.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04633 | +25.97 % | DETECTED_EARLY | NONE | NONE |
| NOM-EUR | 0.0024393 | +19.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.16485 | +18.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.51159 | +18.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0696963 | +16.47 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1934 scans ; 827698 observations ; 1501 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
