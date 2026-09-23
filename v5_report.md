# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T19:49:19.317669+00:00
État : OK | marchés EUR : 426 | V4 : 410 | données valides : 426
Récupération : 2026-09-23T19:48:43.646251+00:00 | âge ticker : 158.1 s | durée : 159.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- BOB-EUR : 0.0047716 € ; score 93.76/100 ; SURVEILLE ; seuil achat non atteint
- AERO-EUR : 0.59938 € ; score 91.66/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 53.813 € ; score 83.72/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : 0.201 € ; score 82.45/100 ; SURVEILLE ; seuil achat non atteint
- USELESS-EUR : 0.263147 € ; score 80.34/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.043961 | +31.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.031975 | +28.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.017885 | +24.09 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| NIL-EUR | 0.086592 | +23.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.86034 | +20.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.3487 | +14.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.15289 | +14.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LIGHTER-EUR | 4.8096 | +13.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.30619 | +12.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALLO-EUR | 0.25899 | +9.56 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1293 scans ; 553555 observations ; 666 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
