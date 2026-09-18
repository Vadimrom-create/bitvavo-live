# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T15:36:05.050475+00:00
État : OK | marchés EUR : 427 | V4 : 377 | données valides : 12
Récupération : 2026-09-18T15:35:36.415123+00:00 | âge ticker : 139.0 s | durée : 139.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 52/427 ; 15 min 84/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LDO-EUR : CHASE_RISK, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- LTC-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- VET-EUR : STALE_DAILY_PROFILE

## SURVEILLE

- HBAR-EUR : 0.068742 € ; score 76.04/100 ; SURVEILLE ; STABILITY_HOLD
- LINK-EUR : 10.6144 € ; score 74.45/100 ; SURVEILLE ; STABILITY_HOLD
- PUMP-EUR : 0.0037435 € ; score 72.21/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 96.283 € ; score 69.91/100 ; SURVEILLE ; STABILITY_HOLD
- DOGE-EUR : 0.076144 € ; score 68.23/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0076722 | +97.09 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| F-EUR | 0.004613 | +65.33 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| CNPY-EUR | 0.4727 | +39.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.2123 | +29.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STRK-EUR | 0.031165 | +28.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.18206 | +26.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.5892 | +21.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.12303 | +21.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.044016 | +20.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.02767 | +19.51 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 807 scans ; 346368 observations ; 166 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
