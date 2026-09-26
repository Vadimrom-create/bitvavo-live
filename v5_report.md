# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T14:58:23.196742+00:00
État : OK | marchés EUR : 427 | V4 : 382 | données valides : 427
Récupération : 2026-09-26T14:57:55.393475+00:00 | âge ticker : 141.0 s | durée : 141.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : 0.22334 € | IGNITION | score 85.59/100 | entrée 7.45/10
  Entrée 0.22334 € ; stop 0.21546 € ; TP1 0.2391 € ; TP2 0.24698 € ; montant 250.00 € ; risque théorique 10.54 € ; R/R net 1.50.
  Chase risk : 2.575/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- RENDER-EUR : 1.7813 € | IGNITION | score 84.54/100 | entrée 7.60/10
  Entrée 1.7797 € ; stop 1.7135 € ; TP1 1.9121 € ; TP2 1.9783 € ; montant 250.00 € ; risque théorique 11.02 € ; R/R net 1.52.
  Chase risk : 1.368/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ICP-EUR : 2.867 € ; score 93.95/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.104889 € ; score 93.13/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : 12.6414 € ; score 92.19/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- CAKE-EUR : 2.4381 € ; score 91.95/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- VVV-EUR : 26.5597 € ; score 91.20/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0018548 | +113.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.020169 | +64.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.118723 | +37.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0005822 | +31.72 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.065068 | +30.57 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.24008 | +21.65 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KMNO-EUR | 0.04504 | +18.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.65725 | +16.97 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| QNT-EUR | 97.248 | +16.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ACE-EUR | 0.19713 | +16.36 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1540 scans ; 658948 observations ; 1000 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
