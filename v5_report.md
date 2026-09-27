# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T16:53:44.745005+00:00
État : OK | marchés EUR : 427 | V4 : 382 | données valides : 427
Récupération : 2026-09-27T16:53:10.688200+00:00 | âge ticker : 148.0 s | durée : 149.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVNT-EUR : INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PTB-EUR : 0.0009001 € ; score 85.96/100 ; SURVEILLE ; WICK_SETUP
- BIGTIME-EUR : 0.008433 € ; score 84.65/100 ; SURVEILLE ; seuil achat non atteint
- AEVO-EUR : 0.023857 € ; score 84.53/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- BAT-EUR : 0.08481 € ; score 84.22/100 ; SURVEILLE ; WICK_SETUP
- AVNT-EUR : 0.11274 € ; score 84.04/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SOON-EUR | 0.30004 | +57.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 163.2 | +54.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.96913 | +33.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.016673 | +31.16 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARX-EUR | 0.25799 | +27.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.007387 | +21.76 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| W-EUR | 0.01366 | +20.68 % | DETECTED_EARLY | NONE | NONE |
| INX-EUR | 0.006322 | +20.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.54974 | +16.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRAM-EUR | 1.51 | +13.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1631 scans ; 697805 observations ; 1160 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
