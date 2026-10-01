# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T01:21:39.199533+00:00
État : OK | marchés EUR : 430 | V4 : 393 | données valides : 430
Récupération : 2026-10-01T01:21:03.959667+00:00 | âge ticker : 150.0 s | durée : 151.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- PLUME-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ONDO-EUR : 0.45038 € ; score 92.38/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : 0.20359 € ; score 92.07/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.20793 € ; score 91.94/100 ; SURVEILLE ; WICK_SETUP
- SUI-EUR : 1.0437 € ; score 91.48/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : 0.065362 € ; score 90.09/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.045 | +83.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.35474 | +48.43 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.008801 | +28.22 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TRAC-EUR | 0.40465 | +21.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.34011 | +21.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.028534 | +19.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.43819 | +17.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0609168 | +14.28 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NOM-EUR | 0.0021083 | +12.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.45117 | +12.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1876 scans ; 802758 observations ; 1429 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
