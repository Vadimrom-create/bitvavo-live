# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T03:01:51.375267+00:00
État : OK | marchés EUR : 427 | V4 : 393 | données valides : 20
Récupération : 2026-09-19T03:01:23.627441+00:00 | âge ticker : 149.2 s | durée : 150.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 22/427 ; 15 min 59/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INVALID_5M
- ICP-EUR : WICK_SETUP, INVALID_15M, INVALID_5M
- NPC-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- PYTH-EUR : INVALID_15M, INVALID_5M
- ADA-EUR : 0.20376 € | IGNITION | score 87.72/100 | entrée 8.20/10
  Entrée 0.20407 € ; stop 0.19444 € ; TP1 0.22333 € ; TP2 0.23296 € ; montant 222.12 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 4.509/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ONDO-EUR : 0.35465 € | IGNITION | score 87.35/100 | entrée 7.15/10
  Entrée 0.3555 € ; stop 0.34248 € ; TP1 0.38153 € ; TP2 0.39455 € ; montant 250.00 € ; risque théorique 10.87 € ; R/R net 1.52.
  Chase risk : 2.186/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ENSO-EUR : 0.8455 € ; score 85.70/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 81.985 € ; score 79.84/100 ; SURVEILLE ; WICK_SETUP
- LINK-EUR : 10.8266 € ; score 79.83/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 222.83 € ; score 79.46/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0066012 | +52.57 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.037151 | +43.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0038502 | +35.22 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.282 | +25.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.053644 | +21.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.18951 | +21.62 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| S-EUR | 0.029652 | +20.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QKC-EUR | 0.0025183 | +20.62 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZIG-EUR | 0.044388 | +19.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MORPHO-EUR | 2.34706 | +17.35 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 854 scans ; 366437 observations ; 186 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
