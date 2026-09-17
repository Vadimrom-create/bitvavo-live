# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-17T01:00:02.962422+00:00
État : OK | marchés EUR : 430 | V4 : 379 | données valides : 6
Récupération : 2026-09-17T00:59:36.213279+00:00 | âge ticker : 137.3 s | durée : 138.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 22/430 ; 15 min 46/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- TAO-EUR : WICK_SETUP, STABILITY_HOLD, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.0006135 € ; score 90.00/100 ; SURVEILLE ; seuil achat non atteint
- BTC-EUR : 66576 € ; score 78.25/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.32473 € ; score 77.20/100 ; SURVEILLE ; STABILITY_HOLD
- LINK-EUR : 9.6066 € ; score 77.14/100 ; SURVEILLE ; STABILITY_HOLD
- UNI-EUR : 5.8056 € ; score 73.17/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.146283 | +75.43 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LSK-EUR | 0.44754 | +31.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DGB-EUR | 0.0038135 | +23.99 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FOLD-EUR | 0.053091 | +21.68 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LIGHTER-EUR | 4.1361 | +17.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.003987 | +15.23 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| IOST-EUR | 0.0007372 | +15.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRAC-EUR | 0.309 | +15.06 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| RAY-EUR | 1.23609 | +14.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 2.3299 | +14.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 673 scans ; 288784 observations ; 112 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
