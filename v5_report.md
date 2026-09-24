# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T17:58:28.879909+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-24T17:57:50.858105+00:00 | âge ticker : 163.4 s | durée : 164.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- TAIKO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ACE-EUR : 0.15745 € ; score 89.33/100 ; SURVEILLE ; seuil achat non atteint
- DATAIP-EUR : 0.1944 € ; score 89.26/100 ; SURVEILLE ; seuil achat non atteint
- PORTAL-EUR : 0.015731 € ; score 86.51/100 ; SURVEILLE ; seuil achat non atteint
- EUL-EUR : 1.2593 € ; score 86.22/100 ; SURVEILLE ; STABILITY_HOLD
- PROM-EUR : 4.7409 € ; score 86.01/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| XAI-EUR | 0.0106581 | +55.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0020028 | +33.81 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LSK-EUR | 0.35322 | +33.23 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.45823 | +25.64 % | DETECTED_EARLY | NONE | NONE |
| ARX-EUR | 0.23058 | +20.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 74.986 | +19.67 % | DETECTED_EARLY | NONE | NONE |
| LTC-EUR | 63.47 | +19.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.035617 | +18.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.102425 | +18.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PLUME-EUR | 0.0161367 | +17.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1373 scans ; 587639 observations ; 742 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
