# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T13:33:04.381941+00:00
État : OK | marchés EUR : 427 | V4 : 392 | données valides : 34
Récupération : 2026-09-19T13:32:31.137022+00:00 | âge ticker : 157.8 s | durée : 159.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 37/427 ; 15 min 84/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- SENT-EUR : STABILITY_HOLD, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- XLM-EUR : 0.17403 € | IGNITION | score 88.81/100 | entrée 7.65/10
  Entrée 0.17417 € ; stop 0.16745 € ; TP1 0.18761 € ; TP2 0.19433 € ; montant 250.00 € ; risque théorique 11.36 € ; R/R net 1.54.
  Chase risk : 4.684/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ONDO-EUR : 0.36808 € | IGNITION | score 82.21/100 | entrée 7.60/10
  Entrée 0.36872 € ; stop 0.35378 € ; TP1 0.3986 € ; TP2 0.41354 € ; montant 250.00 € ; risque théorique 11.84 € ; R/R net 1.56.
  Chase risk : 4.372/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- HYPE-EUR : 80.227 € ; score 78.31/100 ; SURVEILLE ; seuil achat non atteint
- DOGE-EUR : 0.076992 € ; score 77.09/100 ; SURVEILLE ; seuil achat non atteint
- PEPE-EUR : 3.3095e-06 € ; score 76.24/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 229.65 € ; score 76.22/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 96.904 € ; score 74.81/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.067563 | +39.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.215 | +38.14 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EDGE-EUR | 0.077703 | +32.30 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.039296 | +32.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HEI-EUR | 0.147657 | +29.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.022772 | +29.08 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| F-EUR | 0.0037084 | +27.44 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.2995 | +25.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.38059 | +21.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.17176 | +20.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 892 scans ; 382663 observations ; 198 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
