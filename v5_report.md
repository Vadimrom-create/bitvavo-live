# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T01:57:35.477341+00:00
État : OK | marchés EUR : 427 | V4 : 395 | données valides : 23
Récupération : 2026-09-19T01:57:03.640480+00:00 | âge ticker : 149.0 s | durée : 149.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 24/427 ; 15 min 67/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : WICK_SETUP, CHASE_RISK, INVALID_15M, INVALID_5M
- PYTH-EUR : INVALID_15M, INVALID_5M
- WLD-EUR : INVALID_5M

## SURVEILLE

- HYPE-EUR : 81.155 € ; score 78.10/100 ; SURVEILLE ; WICK_SETUP
- ENA-EUR : 0.14945 € ; score 74.72/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- FET-EUR : 0.16015 € ; score 74.09/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.34855 € ; score 73.03/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0062744 | +45.67 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.036525 | +42.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0038627 | +35.94 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.055365 | +27.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QKC-EUR | 0.0025254 | +23.99 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SYN-EUR | 0.191367 | +22.48 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| S-EUR | 0.028944 | +20.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.0442 | +20.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SKY-EUR | 0.062583 | +20.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APT-EUR | 0.6461 | +20.07 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 850 scans ; 364729 observations ; 185 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
