# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T14:36:17.182220+00:00
État : OK | marchés EUR : 430 | V4 : 385 | données valides : 430
Récupération : 2026-10-01T14:35:40.203518+00:00 | âge ticker : 161.2 s | durée : 162.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SYRUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : INSUFFICIENT_NET_RISK_REWARD
- AAVE-EUR : 150.42 € | IGNITION | score 87.50/100 | entrée 6.75/10
  Entrée 150.34 € ; stop 143.22 € ; TP1 164.58 € ; TP2 171.7 € ; montant 221.43 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 4.399/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- SYRUP-EUR : 0.20736 € ; score 88.81/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : 8.0883 € ; score 88.58/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 272.93 € ; score 85.68/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- C-EUR : 0.081816 € ; score 82.32/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP
- ZIG-EUR : 0.049754 € ; score 81.45/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00058728 | +125.51 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.318 | +63.98 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CT-EUR | 0.44233 | +38.21 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CAP-EUR | 0.0735467 | +32.23 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SYN-EUR | 0.179676 | +23.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.028681 | +18.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AUDIO-EUR | 0.01619 | +17.28 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOS-EUR | 0.46556 | +16.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HEI-EUR | 0.13947 | +15.05 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| JASMY-EUR | 0.0051 | +14.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1913 scans ; 818668 observations ; 1478 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
