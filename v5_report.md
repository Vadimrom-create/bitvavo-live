# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T16:22:16.725708+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-22T16:21:42.280472+00:00 | âge ticker : 150.3 s | durée : 152.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVNT-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ETC-EUR : 8.0423 € ; score 88.17/100 ; SURVEILLE ; WICK_SETUP
- AXS-EUR : 0.9456 € ; score 87.70/100 ; SURVEILLE ; seuil achat non atteint
- THE-EUR : 0.07338 € ; score 86.00/100 ; SURVEILLE ; seuil achat non atteint
- AVNT-EUR : 0.10398 € ; score 85.93/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FLUX-EUR : 0.05669 € ; score 84.93/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CHR-EUR | 0.02221 | +46.14 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NIL-EUR | 0.072128 | +26.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.079683 | +24.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BCH-EUR | 282.22 | +22.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.049971 | +20.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.46782 | +15.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.12 | +15.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.37254 | +14.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.1589 | +11.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVA-EUR | 0.23082 | +11.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1197 scans ; 512659 observations ; 512 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
