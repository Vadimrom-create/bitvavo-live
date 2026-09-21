# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T15:15:05.209507+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-21T15:14:08.224290+00:00 | âge ticker : 172.7 s | durée : 173.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- STX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0077972 € | IGNITION | score 82.52/100 | entrée 7.15/10
  Entrée 0.0078101 € ; stop 0.0074475 € ; TP1 0.0085353 € ; TP2 0.0088979 € ; montant 225.29 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 2.72/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LIGHTER-EUR : 4.3861 € ; score 91.02/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- GRASS-EUR : 0.33077 € ; score 87.37/100 ; SURVEILLE ; WICK_SETUP
- DOT-EUR : 1.0364 € ; score 87.01/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- NOM-EUR : 0.0015541 € ; score 85.59/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- BNB-EUR : 702.72 € ; score 84.16/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.053867 | +63.93 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.044549 | +41.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AIOZ-EUR | 0.102215 | +34.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.05818 | +32.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.23727 | +29.73 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0009127 | +28.91 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZRC-EUR | 0.00096 | +26.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.030732 | +26.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WIF-EUR | 0.21714 | +26.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.051946 | +24.80 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1085 scans ; 464947 observations ; 383 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
