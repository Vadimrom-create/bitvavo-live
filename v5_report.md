# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-05T21:24:02.216605+00:00
État : OK | marchés EUR : 427 | V4 : 373 | données valides : 427
Récupération : 2026-10-05T21:22:55.388221+00:00 | âge ticker : 192.5 s | durée : 193.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : 0.51827 € | IGNITION | score 81.00/100 | entrée 7.60/10
  Entrée 0.51817 € ; stop 0.49765 € ; TP1 0.55921 € ; TP2 0.57973 € ; montant 250.00 € ; risque théorique 11.62 € ; R/R net 1.55.
  Chase risk : 4.156/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- BAT-EUR : 0.09435 € ; score 81.53/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.2267 € ; score 80.51/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AXS-EUR : 1.1509 € ; score 80.13/100 ; SURVEILLE ; seuil achat non atteint
- ICP-EUR : 3.1729 € ; score 79.30/100 ; SURVEILLE ; seuil achat non atteint
- ADA-EUR : 0.24019 € ; score 78.90/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| RLC-EUR | 0.59362 | +84.16 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZEUS-EUR | 0.0036134 | +76.26 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RAD-EUR | 0.30952 | +31.05 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NIL-EUR | 0.099417 | +29.19 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FLUID-EUR | 1.9352 | +23.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.167999 | +21.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVR-EUR | 1.776 | +16.52 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| EDU-EUR | 0.05437 | +16.40 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PNT-EUR | 0.057018 | +15.67 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CARV-EUR | 0.045533 | +14.58 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2076 scans ; 888368 observations ; 1639 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
