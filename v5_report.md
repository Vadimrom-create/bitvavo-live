# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T10:47:08.227704+00:00
État : OK | marchés EUR : 428 | V4 : 395 | données valides : 428
Récupération : 2026-09-29T10:46:36.571281+00:00 | âge ticker : 156.4 s | durée : 157.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- GALA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MOVR-EUR : 0.8888 € ; score 90.90/100 ; SURVEILLE ; WICK_SETUP
- RAY-EUR : 1.68381 € ; score 87.70/100 ; SURVEILLE ; WICK_SETUP
- LINK-EUR : 13.5067 € ; score 87.50/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MIOTA-EUR : 0.0493 € ; score 86.81/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- VET-EUR : 0.0079259 € ; score 86.80/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0019 | +55.60 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NMR-EUR | 11.7946 | +27.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 0G-EUR | 0.26629 | +21.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.60167 | +20.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.002134 | +20.01 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SYRUP-EUR | 0.21815 | +19.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CRV-EUR | 0.34651 | +19.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELO-EUR | 0.095492 | +18.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.087905 | +16.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CVX-EUR | 2.061 | +16.35 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1763 scans ; 754237 observations ; 1300 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
