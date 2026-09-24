# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T20:09:28.808220+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-24T20:09:01.273303+00:00 | âge ticker : 147.8 s | durée : 149.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ARB-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAIKO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.19781 € | IGNITION | score 79.57/100 | entrée 6.80/10
  Entrée 0.19782 € ; stop 0.18977 € ; TP1 0.21392 € ; TP2 0.22197 € ; montant 250.00 € ; risque théorique 11.89 € ; R/R net 1.56.
  Chase risk : 5.07/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- VVV-EUR : 27.9206 € | IGNITION | score 76.37/100 | entrée 6.90/10
  Entrée 27.9183 € ; stop 26.3649 € ; TP1 31.0251 € ; TP2 32.5785 € ; montant 192.17 € ; risque théorique 12.00 € ; R/R net 1.66.
  Chase risk : 5.569/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ZIG-EUR : 0.045422 € ; score 92.40/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : 8.1997 € ; score 92.38/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 261.94 € ; score 91.46/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ARB-EUR : 0.19434 € ; score 91.23/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- IOST-EUR : 0.0008095 € ; score 90.79/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| XAI-EUR | 0.0096335 | +40.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.38031 | +35.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.632 | +34.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.45124 | +24.57 % | DETECTED_EARLY | NONE | NONE |
| NOM-EUR | 0.0019859 | +22.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 76.07 | +21.90 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.094282 | +21.09 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.036951 | +19.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0160305 | +18.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.16507 | +18.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1384 scans ; 592336 observations ; 758 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
