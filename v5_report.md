# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T03:02:16.574217+00:00
État : OK | marchés EUR : 426 | V4 : 375 | données valides : 426
Récupération : 2026-09-21T03:01:42.005025+00:00 | âge ticker : 155.5 s | durée : 156.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.15636 € | IGNITION | score 86.37/100 | entrée 7.25/10
  Entrée 0.15676 € ; stop 0.14989 € ; TP1 0.1705 € ; TP2 0.17737 € ; montant 236.82 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 2.639/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- TAO-EUR : 233.88 € ; score 90.07/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SPK-EUR : 0.018151 € ; score 88.84/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- XPL-EUR : 0.083708 € ; score 82.03/100 ; SURVEILLE ; seuil achat non atteint
- ALGO-EUR : 0.095759 € ; score 81.61/100 ; SURVEILLE ; seuil achat non atteint
- HUMA-EUR : 0.01978 € ; score 81.07/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PTB-EUR | 0.0011033 | +80.07 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.261 | +43.65 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.031021 | +38.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.055005 | +26.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VVV-EUR | 28.6621 | +25.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.030251 | +24.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.49428 | +22.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NEAR-EUR | 3.714 | +21.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| S-EUR | 0.033371 | +19.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.4691 | +18.88 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 1042 scans ; 446629 observations ; 296 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
