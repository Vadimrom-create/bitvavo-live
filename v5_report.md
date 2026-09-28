# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T01:48:08.055800+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-28T01:47:10.408346+00:00 | âge ticker : 181.0 s | durée : 181.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- CC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.50329 € | IGNITION | score 81.72/100 | entrée 7.00/10
  Entrée 0.50325 € ; stop 0.48375 € ; TP1 0.54224 € ; TP2 0.56174 € ; montant 250.00 € ; risque théorique 11.40 € ; R/R net 1.54.
  Chase risk : 2.485/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- HBAR-EUR : 0.085251 € ; score 88.82/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.105612 € ; score 87.82/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- CC-EUR : 0.12342 € ; score 86.02/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : 0.11322 € ; score 85.69/100 ; SURVEILLE ; WICK_SETUP
- EGLD-EUR : 4.0931 € ; score 84.82/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 232.072 | +48.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.27393 | +32.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.030643 | +27.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 1.04919 | +26.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IRYS-EUR | 0.017438 | +19.30 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| INX-EUR | 0.006166 | +18.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.074563 | +17.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0045211 | +17.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.013308 | +13.84 % | DETECTED_EARLY | NONE | NONE |
| TRUST-EUR | 0.060799 | +13.54 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1663 scans ; 711469 observations ; 1215 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
