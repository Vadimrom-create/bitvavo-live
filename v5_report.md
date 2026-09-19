# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T09:26:00.024411+00:00
État : OK | marchés EUR : 427 | V4 : 393 | données valides : 31
Récupération : 2026-09-19T09:25:32.403956+00:00 | âge ticker : 148.0 s | durée : 148.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 36/427 ; 15 min 75/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INVALID_5M
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 228.32 € | IGNITION | score 90.53/100 | entrée 7.40/10
  Entrée 228.37 € ; stop 218.02 € ; TP1 249.07 € ; TP2 259.41 € ; montant 230.05 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 4.244/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- RAY-EUR : 1.62094 € | IGNITION | score 89.88/100 | entrée 7.55/10
  Entrée 1.61522 € ; stop 1.52415 € ; TP1 1.79736 € ; TP2 1.88843 € ; montant 189.92 € ; risque théorique 12.00 € ; R/R net 1.67.
  Chase risk : 4.769/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ONDO-EUR : 0.35199 € ; score 91.06/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 80.286 € ; score 81.28/100 ; SURVEILLE ; seuil achat non atteint
- PEPE-EUR : 3.2777e-06 € ; score 79.76/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.15858 € ; score 76.99/100 ; SURVEILLE ; WICK_SETUP
- BTC-EUR : 70866 € ; score 75.94/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.224888 | +44.97 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| HEI-EUR | 0.156428 | +36.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.065474 | +36.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.077133 | +33.67 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| F-EUR | 0.0036755 | +27.51 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.29668 | +26.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.046782 | +25.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.023111 | +23.02 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| STRK-EUR | 0.037293 | +19.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INJ-EUR | 6.5074 | +17.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 877 scans ; 376258 observations ; 190 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
