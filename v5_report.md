# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T11:00:05.588928+00:00
État : OK | marchés EUR : 427 | V4 : 395 | données valides : 427
Récupération : 2026-09-28T10:59:33.557488+00:00 | âge ticker : 159.2 s | durée : 160.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- GRAM-EUR : 1.4777 € | IGNITION | score 88.55/100 | entrée 7.80/10
  Entrée 1.4755 € ; stop 1.4002 € ; TP1 1.6261 € ; TP2 1.7014 € ; montant 207.42 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 3.778/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LTC-EUR : 62.845 € ; score 92.84/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : 12.2373 € ; score 86.72/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- USDC-EUR : 0.8794 € ; score 85.23/100 ; SURVEILLE ; seuil achat non atteint
- AXL-EUR : 0.045889 € ; score 84.27/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- ALGO-EUR : 0.112164 € ; score 83.99/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 203.187 | +35.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HBAR-EUR | 0.101786 | +22.45 % | DETECTED_EARLY | NONE | NONE |
| GRT-EUR | 0.028203 | +15.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AUDIO-EUR | 0.0146 | +11.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XDC-EUR | 0.030545 | +11.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NMR-EUR | 9.3517 | +9.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AZTEC-EUR | 0.016234 | +9.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALGO-EUR | 0.112164 | +8.61 % | DETECTED_EARLY | NONE | NONE |
| PUMP-EUR | 0.0042276 | +7.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.2751 | +7.06 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1690 scans ; 722998 observations ; 1243 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
