# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T19:39:08.256048+00:00
État : OK | marchés EUR : 426 | V4 : 384 | données valides : 426
Récupération : 2026-09-20T19:38:30.822687+00:00 | âge ticker : 155.1 s | durée : 156.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- AIOZ-EUR : 0.080142 € | IGNITION | score 81.21/100 | entrée 5.55/10
  Entrée 0.080355 € ; stop 0.076936 € ; TP1 0.087192 € ; TP2 0.090611 € ; montant 242.92 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 4.23/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- T-EUR : 0.0044412 € ; score 92.10/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- RUNE-EUR : 0.48842 € ; score 88.85/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP, STABILITY_HOLD
- JTO-EUR : 0.44083 € ; score 87.69/100 ; SURVEILLE ; seuil achat non atteint
- JUP-EUR : 0.24379 € ; score 82.98/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- COW-EUR : 0.13537 € ; score 82.94/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.032784 | +50.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.232 | +26.22 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0007762 | +25.07 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SKL-EUR | 0.0042857 | +21.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.03359 | +19.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.051493 | +16.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.043016 | +16.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.5447 | +15.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CELR-EUR | 0.0030401 | +15.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| C-EUR | 0.072039 | +14.66 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1011 scans ; 433423 observations ; 247 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
