# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T03:38:11.949041+00:00
État : OK | marchés EUR : 427 | V4 : 394 | données valides : 20
Récupération : 2026-09-19T03:37:42.788090+00:00 | âge ticker : 153.1 s | durée : 155.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 21/427 ; 15 min 58/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INVALID_5M
- LTC-EUR : INVALID_5M
- PUMP-EUR : STABILITY_HOLD, INVALID_5M
- PYTH-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M
- TAO-EUR : 224.61 € | IGNITION | score 89.05/100 | entrée 7.40/10
  Entrée 224.62 € ; stop 215.61 € ; TP1 242.64 € ; TP2 251.64 € ; montant 250.00 € ; risque théorique 11.74 € ; R/R net 1.55.
  Chase risk : 3.104/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- APT-EUR : 0.6607 € ; score 79.39/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 81.489 € ; score 79.15/100 ; SURVEILLE ; WICK_SETUP
- SOL-EUR : 98.364 € ; score 74.79/100 ; SURVEILLE ; WICK_SETUP
- ONDO-EUR : 0.35346 € ; score 72.88/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0070905 | +69.14 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.038161 | +42.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0038593 | +35.54 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SYN-EUR | 0.192053 | +25.69 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.28133 | +24.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.060198 | +20.56 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZIG-EUR | 0.044388 | +19.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QKC-EUR | 0.0024934 | +19.43 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.053066 | +18.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INJ-EUR | 5.9462 | +17.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 856 scans ; 367291 observations ; 186 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
