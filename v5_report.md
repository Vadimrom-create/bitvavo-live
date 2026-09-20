# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T01:50:35.378097+00:00
État : OK | marchés EUR : 427 | V4 : 392 | données valides : 25
Récupération : 2026-09-20T01:50:04.718829+00:00 | âge ticker : 155.1 s | durée : 156.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 26/427 ; 15 min 65/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : WICK_SETUP, INVALID_5M
- POL-EUR : STABILITY_HOLD, INVALID_5M
- PYTH-EUR : WICK_SETUP, INVALID_5M
- UNI-EUR : WICK_SETUP, CHASE_RISK, INVALID_5M

## SURVEILLE

- VET-EUR : 0.0074827 € ; score 77.51/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 95.775 € ; score 76.28/100 ; SURVEILLE ; WICK_SETUP
- TAO-EUR : 229.03 € ; score 68.96/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0035913 | +80.06 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| G-EUR | 0.0099266 | +57.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.07106 | +28.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.18346 | +21.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.074699 | +20.48 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| INJ-EUR | 6.9937 | +19.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SKL-EUR | 0.0040948 | +18.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIL-EUR | 0.0031896 | +17.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOLV-EUR | 0.0040127 | +17.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.30284 | +14.51 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 941 scans ; 403586 observations ; 223 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
