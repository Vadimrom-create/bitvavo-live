# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T16:50:14.540245+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 35
Récupération : 2026-09-19T16:49:42.189705+00:00 | âge ticker : 153.0 s | durée : 154.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 39/427 ; 15 min 85/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- KAS-EUR : WICK_SETUP, INVALID_5M
- WAL-EUR : WICK_SETUP, INVALID_5M
- PEPE-EUR : 3.5051e-06 € | IGNITION | score 86.42/100 | entrée 7.55/10
  Entrée 3.5085e-06 € ; stop 3.2888e-06 € ; TP1 3.9479e-06 € ; TP2 4.1675e-06 € ; montant 172.91 € ; risque théorique 12.00 € ; R/R net 1.70.
  Chase risk : 5.742/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- HYPE-EUR : 80.836 € ; score 78.74/100 ; SURVEILLE ; WICK_SETUP
- SOL-EUR : 97.295 € ; score 75.85/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- ONDO-EUR : 0.37791 € ; score 75.77/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- TAO-EUR : 235.4 € ; score 74.13/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- SUI-EUR : 0.74318 € ; score 72.87/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0103935 | +41.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.071762 | +38.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.209909 | +34.78 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.31613 | +30.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.3999 | +26.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.17566 | +22.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.021991 | +22.38 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| AIOZ-EUR | 0.080244 | +21.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.071038 | +21.39 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.038684 | +20.89 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 905 scans ; 388214 observations ; 210 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
