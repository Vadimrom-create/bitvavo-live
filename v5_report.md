# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T15:51:31.375494+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-26T15:51:02.099501+00:00 | âge ticker : 146.0 s | durée : 146.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- AXS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- STX-EUR : INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : 1.1149 € | IGNITION | score 93.49/100 | entrée 7.80/10
  Entrée 1.1149 € ; stop 1.0704 € ; TP1 1.2039 € ; TP2 1.2484 € ; montant 250.00 € ; risque théorique 11.69 € ; R/R net 1.55.
  Chase risk : 4.483/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ALGO-EUR : 0.106657 € | IGNITION | score 86.01/100 | entrée 6.90/10
  Entrée 0.106778 € ; stop 0.102444 € ; TP1 0.115446 € ; TP2 0.11978 € ; montant 250.00 € ; risque théorique 11.86 € ; R/R net 1.56.
  Chase risk : 4.634/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- VIRTUAL-EUR : 0.71897 € | IGNITION | score 83.37/100 | entrée 7.35/10
  Entrée 0.71821 € ; stop 0.68566 € ; TP1 0.78331 € ; TP2 0.81585 € ; montant 8.53 € ; risque théorique 0.44 € ; R/R net 1.60.
  Chase risk : 4.276/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- GALA-EUR : 0.0019904 € ; score 92.98/100 ; SURVEILLE ; WICK_SETUP
- STX-EUR : 0.30231 € ; score 92.88/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- UMA-EUR : 0.38444 € ; score 92.83/100 ; SURVEILLE ; seuil achat non atteint
- RSR-EUR : 0.0015879 € ; score 91.77/100 ; SURVEILLE ; seuil achat non atteint
- ADA-EUR : 0.22729 € ; score 91.45/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017091 | +105.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.12074 | +39.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006054 | +36.97 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 104.006 | +24.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019776 | +24.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.062615 | +23.91 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| HUMA-EUR | 0.027014 | +21.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.044108 | +19.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ACE-EUR | 0.19969 | +18.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RUNE-EUR | 0.66204 | +18.16 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1543 scans ; 660229 observations ; 1012 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
