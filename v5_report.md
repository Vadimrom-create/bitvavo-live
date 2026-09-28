# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T22:23:59.649549+00:00
État : OK | marchés EUR : 428 | V4 : 400 | données valides : 428
Récupération : 2026-09-28T22:23:26.464593+00:00 | âge ticker : 148.6 s | durée : 149.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ROSE-EUR : 0.007353 € ; score 90.96/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- W-EUR : 0.011967 € ; score 90.73/100 ; SURVEILLE ; seuil achat non atteint
- PLUME-EUR : 0.0158679 € ; score 87.39/100 ; SURVEILLE ; WICK_SETUP
- NPC-EUR : 0.020394 € ; score 85.11/100 ; SURVEILLE ; seuil achat non atteint
- PYTH-EUR : 0.070796 € ; score 83.62/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 12.2313 | +38.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.107473 | +29.65 % | DETECTED_EARLY | NONE | NONE |
| ALGO-EUR | 0.119036 | +15.00 % | DETECTED_EARLY | NONE | NONE |
| MIOTA-EUR | 0.048691 | +10.33 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| IKA-EUR | 0.001813 | +8.69 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LINK-EUR | 13.243 | +7.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AZTEC-EUR | 0.016417 | +6.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.30191 | +5.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0490275 | +4.83 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| XLM-EUR | 0.19727 | +4.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1725 scans ; 737973 observations ; 1268 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
