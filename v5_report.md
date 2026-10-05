# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-05T22:28:50.793773+00:00
État : OK | marchés EUR : 427 | V4 : 373 | données valides : 427
Récupération : 2026-10-05T22:28:15.105014+00:00 | âge ticker : 152.2 s | durée : 153.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ENS-EUR : 6.152 € ; score 84.41/100 ; SURVEILLE ; WICK_SETUP
- FET-EUR : 0.2274 € ; score 83.93/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : 0.02258 € ; score 82.70/100 ; SURVEILLE ; STABILITY_HOLD
- AXS-EUR : 1.1547 € ; score 81.26/100 ; SURVEILLE ; seuil achat non atteint
- ADA-EUR : 0.24387 € ; score 81.20/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| RLC-EUR | 0.66566 | +105.82 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZEUS-EUR | 0.0035585 | +73.59 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RAD-EUR | 0.31994 | +35.46 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NIL-EUR | 0.098221 | +25.62 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FLUID-EUR | 1.8833 | +20.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ORCA-EUR | 2.09399 | +19.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.7779 | +18.55 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| EDU-EUR | 0.05367 | +14.90 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PNT-EUR | 0.056484 | +14.59 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CAP-EUR | 0.0656766 | +13.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique (snapshot asynchrone) : 2083 scans ; 891357 observations ; 1648 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
