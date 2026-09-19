# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T07:17:14.238362+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 30
Récupération : 2026-09-19T07:16:39.820635+00:00 | âge ticker : 162.0 s | durée : 163.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 35/427 ; 15 min 66/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INVALID_5M
- HYPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : CHASE_RISK, INVALID_5M

## SURVEILLE

- HYPE-EUR : 81.188 € ; score 81.11/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : 0.15841 € ; score 78.90/100 ; SURVEILLE ; WICK_SETUP
- SOL-EUR : 97.418 € ; score 77.32/100 ; SURVEILLE ; WICK_SETUP
- APT-EUR : 0.6153 € ; score 75.04/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 222.06 € ; score 72.71/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| EDGE-EUR | 0.083 | +43.78 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.30968 | +34.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.034986 | +28.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.20423 | +28.51 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| F-EUR | 0.003658 | +27.67 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZIG-EUR | 0.047025 | +25.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INJ-EUR | 6.5501 | +24.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| G-EUR | 0.0067107 | +24.43 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.055353 | +21.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HEI-EUR | 0.138397 | +21.54 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 869 scans ; 372842 observations ; 190 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
