# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-16T19:00:02.227241+00:00
État : OK | marchés EUR : 430 | V4 : 382 | données valides : 11
Récupération : 2026-09-16T18:59:31.775142+00:00 | âge ticker : 141.9 s | durée : 142.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 29/430 ; 15 min 56/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETH-EUR : STALE_DAILY_PROFILE
- FET-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- HYPE-EUR : STALE_DAILY_PROFILE
- NEAR-EUR : CHASE_RISK, STALE_DAILY_PROFILE
- SOL-EUR : STALE_DAILY_PROFILE
- UNI-EUR : INVALID_5M, STALE_DAILY_PROFILE
- WLD-EUR : WICK_SETUP, STALE_DAILY_PROFILE

## SURVEILLE

- TAO-EUR : 189.25 € ; score 83.86/100 ; SURVEILLE ; WICK_SETUP
- XLM-EUR : 0.155 € ; score 83.53/100 ; SURVEILLE ; seuil achat non atteint
- DOGE-EUR : 0.069214 € ; score 83.43/100 ; SURVEILLE ; seuil achat non atteint
- XRP-EUR : 1.11298 € ; score 83.41/100 ; SURVEILLE ; seuil achat non atteint
- LINK-EUR : 9.3885 € ; score 81.41/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.158802 | +125.58 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LSK-EUR | 0.6444 | +88.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HEI-EUR | 0.119295 | +23.77 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FOLD-EUR | 0.045865 | +20.70 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.35535 | +17.11 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| RAY-EUR | 1.20759 | +12.84 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ARB-EUR | 0.14158 | +12.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.004047 | +11.49 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| IOST-EUR | 0.0007153 | +9.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZEN-EUR | 5.8799 | +9.39 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 652 scans ; 279754 observations ; 103 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
