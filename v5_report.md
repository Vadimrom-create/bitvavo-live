# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-05T22:01:41.630188+00:00
État : OK | marchés EUR : 427 | V4 : 373 | données valides : 427
Récupération : 2026-10-05T22:01:07.106806+00:00 | âge ticker : 154.5 s | durée : 155.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- API3-EUR : 0.27805 € ; score 83.88/100 ; SURVEILLE ; seuil achat non atteint
- AXS-EUR : 1.1577 € ; score 83.30/100 ; SURVEILLE ; seuil achat non atteint
- SENT-EUR : 0.022183 € ; score 82.53/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.51692 € ; score 82.22/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : 3.2018 € ; score 80.47/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| RLC-EUR | 0.63605 | +96.66 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZEUS-EUR | 0.0036222 | +78.16 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RAD-EUR | 0.30613 | +29.62 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NIL-EUR | 0.098902 | +28.52 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FLUID-EUR | 1.9213 | +22.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PNT-EUR | 0.060364 | +22.46 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MOVR-EUR | 1.7798 | +18.73 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GTC-EUR | 0.168747 | +16.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DIA-EUR | 0.16309 | +14.79 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ORCA-EUR | 2 | +14.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique (snapshot asynchrone) : 2076 scans ; 888368 observations ; 1639 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
