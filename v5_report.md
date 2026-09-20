# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T20:54:05.239135+00:00
État : OK | marchés EUR : 426 | V4 : 381 | données valides : 426
Récupération : 2026-09-20T20:53:31.604240+00:00 | âge ticker : 153.4 s | durée : 154.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : 0.28458 € | IGNITION | score 87.93/100 | entrée 6.80/10
  Entrée 0.28518 € ; stop 0.27445 € ; TP1 0.30663 € ; TP2 0.31736 € ; montant 250.00 € ; risque théorique 11.12 € ; R/R net 1.53.
  Chase risk : 1.725/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CAKE-EUR : 2.2408 € ; score 91.57/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- RAY-EUR : 1.46488 € ; score 91.43/100 ; SURVEILLE ; WICK_SETUP
- IO-EUR : 0.12707 € ; score 88.69/100 ; SURVEILLE ; seuil achat non atteint
- W-EUR : 0.010093 € ; score 86.23/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.24661 € ; score 85.99/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.032408 | +49.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.25216 | +37.33 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0007887 | +29.04 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| S-EUR | 0.034873 | +22.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.053898 | +21.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELR-EUR | 0.0030452 | +20.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.641 | +18.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.028071 | +17.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.042936 | +17.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LUNA2-EUR | 0.047795 | +16.13 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 1016 scans ; 435553 observations ; 264 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
