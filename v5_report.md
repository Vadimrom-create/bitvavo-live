# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T08:36:46.247968+00:00
État : OK | marchés EUR : 426 | V4 : 403 | données valides : 426
Récupération : 2026-09-22T08:36:19.955969+00:00 | âge ticker : 143.6 s | durée : 144.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.08336 € | IGNITION | score 86.78/100 | entrée 7.40/10
  Entrée 0.083471 € ; stop 0.080276 € ; TP1 0.089861 € ; TP2 0.093056 € ; montant 250.00 € ; risque théorique 11.29 € ; R/R net 1.53.
  Chase risk : 3.382/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- TAIKO-EUR : 0.08047 € ; score 88.87/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : 1.0426 € ; score 88.57/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- WAL-EUR : 0.030207 € ; score 87.52/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SAND-EUR : 0.037003 € ; score 86.64/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ESP-EUR : 0.083055 € ; score 85.09/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.018943 | +120.37 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014656 | +86.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.119393 | +45.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.057759 | +40.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.39629 | +23.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.3893e-06 | +23.13 % | DETECTED_EARLY | NONE | NONE |
| WIF-EUR | 0.22035 | +21.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.260991 | +21.39 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CARV-EUR | 0.040582 | +18.23 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FORM-EUR | 0.27073 | +16.72 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1168 scans ; 500305 observations ; 469 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
