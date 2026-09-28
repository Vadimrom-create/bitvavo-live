# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T10:43:11.391645+00:00
État : OK | marchés EUR : 427 | V4 : 393 | données valides : 427
Récupération : 2026-09-28T10:42:17.095995+00:00 | âge ticker : 177.9 s | durée : 178.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 63.069 € | IGNITION | score 92.12/100 | entrée 7.85/10
  Entrée 63.146 € ; stop 60.764 € ; TP1 67.91 € ; TP2 70.292 € ; montant 250.00 € ; risque théorique 11.15 € ; R/R net 1.53.
  Chase risk : 1.029/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- GRAM-EUR : 1.4968 € | IGNITION | score 89.05/100 | entrée 7.10/10
  Entrée 1.5021 € ; stop 1.4014 € ; TP1 1.7035 € ; TP2 1.8042 € ; montant 162.59 € ; risque théorique 12.00 € ; R/R net 1.72.
  Chase risk : 6.204/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LINK-EUR : 12.2174 € ; score 90.18/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MAGIC-EUR : 0.046469 € ; score 88.15/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- PYTH-EUR : 0.071739 € ; score 88.00/100 ; SURVEILLE ; seuil achat non atteint
- WELL-EUR : 0.0019616 € ; score 86.74/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- XLM-EUR : 0.18808 € ; score 86.65/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 195.849 | +29.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HBAR-EUR | 0.101731 | +22.23 % | DETECTED_EARLY | NONE | NONE |
| GRT-EUR | 0.028193 | +15.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AUDIO-EUR | 0.014536 | +11.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XDC-EUR | 0.030752 | +11.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALGO-EUR | 0.113432 | +9.70 % | DETECTED_EARLY | NONE | NONE |
| NMR-EUR | 9.2511 | +8.76 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| IMX-EUR | 0.15728 | +7.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0041979 | +6.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.069944 | +6.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1689 scans ; 722571 observations ; 1243 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
