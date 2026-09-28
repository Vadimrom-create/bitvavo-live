# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T05:58:29.826125+00:00
État : OK | marchés EUR : 427 | V4 : 396 | données valides : 427
Récupération : 2026-09-28T05:57:57.681886+00:00 | âge ticker : 154.3 s | durée : 155.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.085498 € | IGNITION | score 87.15/100 | entrée 7.65/10
  Entrée 0.085503 € ; stop 0.082327 € ; TP1 0.091854 € ; TP2 0.09503 € ; montant 250.00 € ; risque théorique 11.00 € ; R/R net 1.52.
  Chase risk : 0/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- KAS-EUR : 0.041607 € | IGNITION | score 80.48/100 | entrée 7.00/10
  Entrée 0.041956 € ; stop 0.040252 € ; TP1 0.045363 € ; TP2 0.047067 € ; montant 250.00 € ; risque théorique 11.87 € ; R/R net 1.56.
  Chase risk : 1.701/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- BCH-EUR : 271.7 € ; score 90.74/100 ; SURVEILLE ; seuil achat non atteint
- CVX-EUR : 1.824 € ; score 84.87/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- NIL-EUR : 0.078552 € ; score 84.48/100 ; SURVEILLE ; seuil achat non atteint
- MOVR-EUR : 0.8796 € ; score 84.14/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- W-EUR : 0.01265 € ; score 83.68/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 235.302 | +54.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 1.13 | +35.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.02856 | +18.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AUDIO-EUR | 0.015178 | +17.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0045151 | +16.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.29941 | +13.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XDC-EUR | 0.030164 | +12.97 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| GRASS-EUR | 0.56669 | +12.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IRYS-EUR | 0.016826 | +12.39 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| ARX-EUR | 0.21792 | +11.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1676 scans ; 717020 observations ; 1237 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
