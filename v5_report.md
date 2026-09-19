# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T08:21:16.231287+00:00
État : OK | marchés EUR : 427 | V4 : 393 | données valides : 33
Récupération : 2026-09-19T08:20:42.899275+00:00 | âge ticker : 156.3 s | durée : 157.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 42/427 ; 15 min 68/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PORTAL-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M
- RAY-EUR : WICK_SETUP, INVALID_5M
- RENDER-EUR : WICK_SETUP, INVALID_5M
- AVAX-EUR : 7.5589 € | IGNITION | score 81.34/100 | entrée 7.60/10
  Entrée 7.5613 € ; stop 7.2848 € ; TP1 8.1143 € ; TP2 8.3908 € ; montant 250.00 € ; risque théorique 10.86 € ; R/R net 1.52.
  Chase risk : 2.724/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- HYPE-EUR : 80.897 € ; score 78.91/100 ; SURVEILLE ; seuil achat non atteint
- ENA-EUR : 0.16124 € ; score 78.73/100 ; SURVEILLE ; WICK_SETUP
- SOL-EUR : 97.35 € ; score 76.33/100 ; SURVEILLE ; WICK_SETUP
- TAO-EUR : 223.19 € ; score 76.04/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- PEPE-EUR : 3.2802e-06 € ; score 74.79/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| EDGE-EUR | 0.087097 | +50.88 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| HEI-EUR | 0.159 | +40.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.217031 | +36.84 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| F-EUR | 0.0037537 | +29.78 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.30038 | +29.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.036541 | +25.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INJ-EUR | 6.7116 | +24.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZAMA-EUR | 0.059971 | +23.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.046175 | +23.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.37493 | +18.98 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 873 scans ; 374550 observations ; 190 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
