# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T03:26:14.231152+00:00
État : OK | marchés EUR : 430 | V4 : 386 | données valides : 430
Récupération : 2026-10-02T03:25:45.119159+00:00 | âge ticker : 152.6 s | durée : 154.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MOVE-EUR : 0.009015 € ; score 90.07/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- WIF-EUR : 0.22693 € ; score 88.20/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- STRK-EUR : 0.03904 € ; score 84.46/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 78.932 € ; score 84.20/100 ; SURVEILLE ; WICK_SETUP
- AAVE-EUR : 154.3 € ; score 83.68/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.000679 | +163.30 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.140183 | +67.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SCR-EUR | 0.029655 | +34.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.44105 | +28.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04821 | +24.19 % | DETECTED_EARLY | NONE | NONE |
| SUPER-EUR | 0.21194 | +18.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALICE-EUR | 0.17523 | +17.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0024468 | +16.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 2.4941 | +16.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.162553 | +16.30 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1952 scans ; 835438 observations ; 1517 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
