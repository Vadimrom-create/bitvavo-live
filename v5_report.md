# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T23:15:11.333053+00:00
État : OK | marchés EUR : 428 | V4 : 399 | données valides : 428
Récupération : 2026-09-28T23:14:38.504174+00:00 | âge ticker : 148.1 s | durée : 149.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- CRV-EUR : 0.32593 € ; score 87.55/100 ; SURVEILLE ; WICK_SETUP
- IO-EUR : 0.13729 € ; score 87.55/100 ; SURVEILLE ; seuil achat non atteint
- PLUME-EUR : 0.0162056 € ; score 87.18/100 ; SURVEILLE ; seuil achat non atteint
- MON-EUR : 0.025161 € ; score 85.73/100 ; SURVEILLE ; WICK_SETUP
- VIRTUAL-EUR : 0.72987 € ; score 85.67/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 12.9813 | +44.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.107177 | +28.97 % | DETECTED_EARLY | NONE | NONE |
| ALGO-EUR | 0.117292 | +12.88 % | DETECTED_EARLY | NONE | NONE |
| 0G-EUR | 0.25124 | +10.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LINK-EUR | 13.4361 | +9.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 1.00181 | +9.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IKA-EUR | 0.0018132 | +8.87 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| MIOTA-EUR | 0.048594 | +8.75 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AZTEC-EUR | 0.016681 | +7.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.04973 | +5.96 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1728 scans ; 739257 observations ; 1270 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
