# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T23:50:11.127729+00:00
État : OK | marchés EUR : 428 | V4 : 399 | données valides : 428
Récupération : 2026-09-28T23:49:40.881763+00:00 | âge ticker : 151.5 s | durée : 152.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BCH-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : 0.728 € | IGNITION | score 89.90/100 | entrée 7.00/10
  Entrée 0.72795 € ; stop 0.70157 € ; TP1 0.7807 € ; TP2 0.80708 € ; montant 250.00 € ; risque théorique 10.78 € ; R/R net 1.51.
  Chase risk : 2.079/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- XLM-EUR : 0.20318 € | IGNITION | score 84.88/100 | entrée 7.30/10
  Entrée 0.20333 € ; stop 0.19561 € ; TP1 0.21877 € ; TP2 0.22649 € ; montant 250.00 € ; risque théorique 11.21 € ; R/R net 1.53.
  Chase risk : 3.025/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CRO-EUR : 0.061418 € ; score 92.21/100 ; SURVEILLE ; SPREAD_RISK
- BCH-EUR : 272.94 € ; score 90.74/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : 1.7089 € ; score 87.75/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : 0.16986 € ; score 87.14/100 ; SURVEILLE ; seuil achat non atteint
- LPT-EUR : 1.5061 € ; score 87.08/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 12.9228 | +43.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.106991 | +26.84 % | DETECTED_EARLY | NONE | NONE |
| ALGO-EUR | 0.118443 | +12.99 % | DETECTED_EARLY | NONE | NONE |
| LINK-EUR | 13.5563 | +9.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 0G-EUR | 0.25432 | +9.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IKA-EUR | 0.0018167 | +9.08 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| CRV-EUR | 0.33735 | +8.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XLM-EUR | 0.20318 | +7.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MIOTA-EUR | 0.0487 | +6.94 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TREAD-EUR | 1.00078 | +6.83 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1730 scans ; 740113 observations ; 1270 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
