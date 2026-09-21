# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T01:54:36.280617+00:00
État : OK | marchés EUR : 426 | V4 : 381 | données valides : 426
Récupération : 2026-09-21T01:54:04.688255+00:00 | âge ticker : 145.6 s | durée : 147.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETHFI-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : 0.081834 € | IGNITION | score 81.04/100 | entrée 6.90/10
  Entrée 0.081618 € ; stop 0.077067 € ; TP1 0.09072 € ; TP2 0.095271 € ; montant 191.80 € ; risque théorique 12.00 € ; R/R net 1.66.
  Chase risk : 8.793/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LPT-EUR : 1.4004 € ; score 87.97/100 ; SURVEILLE ; seuil achat non atteint
- ESP-EUR : 0.082161 € ; score 86.52/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- XTZ-EUR : 0.30614 € ; score 84.85/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK
- PROVE-EUR : 0.20475 € ; score 84.60/100 ; SURVEILLE ; SPREAD_RISK
- HEI-EUR : 0.130823 € ; score 82.50/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PTB-EUR | 0.0010044 | +60.17 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.032766 | +42.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.23903 | +29.00 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.054465 | +23.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.48637 | +23.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.029115 | +20.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.6272 | +17.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| VVV-EUR | 26.83 | +16.75 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| S-EUR | 0.033451 | +15.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.030286 | +15.52 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1038 scans ; 444925 observations ; 287 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
