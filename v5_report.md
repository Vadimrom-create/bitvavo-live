# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-22T04:57:57.512484+00:00
État : OK | marchés EUR : 428 | V4 : 369 | données valides : 428
Récupération : 2026-10-22T04:56:52.705087+00:00 | âge ticker : 175.8 s | durée : 176.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- WLD-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ELSA-EUR : 0.063694 € ; score 73.14/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.49511 € ; score 72.49/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| IRYS-EUR | 0.018649 | +54.76 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ALT-EUR | 0.0107189 | +18.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.059394 | +16.64 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| BILL-EUR | 0.005741 | +14.89 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TRIA-EUR | 0.002508 | +13.84 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PROM-EUR | 5.2241 | +12.84 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| AVA-EUR | 0.32145 | +12.12 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CNPY-EUR | 0.21113 | +10.93 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ELSA-EUR | 0.063694 | +8.53 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| LIGHTER-EUR | 3.2943 | +8.10 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2210 scans ; 945565 observations ; 1661 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
