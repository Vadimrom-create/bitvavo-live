# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T17:03:55.605951+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 35
Récupération : 2026-09-19T17:03:25.288992+00:00 | âge ticker : 152.6 s | durée : 153.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 38/427 ; 15 min 86/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INVALID_5M
- BIGTIME-EUR : INVALID_15M, INVALID_5M
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- VET-EUR : INVALID_5M
- PEPE-EUR : 3.5572e-06 € | IGNITION | score 83.57/100 | entrée 6.85/10
  Entrée 3.5604e-06 € ; stop 3.2929e-06 € ; TP1 4.0954e-06 € ; TP2 4.3629e-06 € ; montant 146.58 € ; risque théorique 12.00 € ; R/R net 1.74.
  Chase risk : 7.548/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- HYPE-EUR : 81.244 € ; score 88.42/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : 97.536 € ; score 77.93/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 234.77 € ; score 74.52/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- ADA-EUR : 0.20026 € ; score 74.39/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- SUI-EUR : 0.7471 € ; score 73.95/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.072965 | +42.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.210373 | +37.45 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| G-EUR | 0.0098725 | +31.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.31337 | +29.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.17844 | +24.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EPIC-EUR | 0.39248 | +24.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FIL-EUR | 0.94142 | +22.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 8.4427 | +20.35 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| EDGE-EUR | 0.07034 | +20.20 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AIOZ-EUR | 0.079674 | +18.13 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 906 scans ; 388641 observations ; 211 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
