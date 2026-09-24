# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T19:18:58.728484+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-24T19:18:26.157174+00:00 | âge ticker : 161.1 s | durée : 162.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- GMT-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : 11.6827 € | IGNITION | score 81.18/100 | entrée 7.60/10
  Entrée 11.679 € ; stop 11.2192 € ; TP1 12.5986 € ; TP2 13.0583 € ; montant 250.00 € ; risque théorique 11.56 € ; R/R net 1.55.
  Chase risk : 4.185/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- GMT-EUR : 0.007667 € ; score 94.30/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BEAM-EUR : 0.0017772 € ; score 87.93/100 ; SURVEILLE ; SPREAD_RISK
- A-EUR : 0.087092 € ; score 87.03/100 ; SURVEILLE ; seuil achat non atteint
- XLM-EUR : 0.18731 € ; score 86.64/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- MOVR-EUR : 0.8031 € ; score 86.35/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| XAI-EUR | 0.0100294 | +44.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.3802 | +36.81 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| NOM-EUR | 0.0019966 | +28.67 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ONDO-EUR | 0.45577 | +26.06 % | DETECTED_EARLY | NONE | NONE |
| PLUME-EUR | 0.0165857 | +22.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 75.83 | +22.02 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.037164 | +21.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XPL-EUR | 0.092171 | +19.19 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| LTC-EUR | 62.527 | +16.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.19975 | +16.92 % | DETECTED_EARLY | NONE | NONE |

Historique : 1378 scans ; 589774 observations ; 757 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
