# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T22:24:19.998524+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 8.344 | entrée 7.450 | trend 8.700 | rang 7.882
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BIGTIME-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.660 | entrée 6.350 | trend 8.450 | rang 7.545
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MERL-EUR | action LATENT_ACCELERATOR | opportunité 8.272 | entrée 5.650 | trend 8.900 | rang 7.890
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COW-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.916 | entrée 7.200 | trend 8.900 | rang 8.364
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.364
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.070
3. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.907

## Accélération indépendante

- AIOZ-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- WIF-EUR — CONFIRMED_ACCELERATION — score 7.699/10 — DETECTED_BUT_TOO_LATE
- AKT-EUR — CONFIRMED_ACCELERATION — score 7.349/10 — DETECTED_BUT_TOO_LATE
- SHIB-EUR — CONFIRMED_ACCELERATION — score 7.226/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — CONFIRMED_ACCELERATION — score 6.769/10 — DETECTED_BUT_TOO_LATE
- DOGE-EUR — BUILDING_ACCELERATION — score 6.449/10 — DETECTED_BUT_TOO_LATE
- SPX-EUR — BUILDING_ACCELERATION — score 6.396/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ETC-EUR — BUILDING_ACCELERATION — score 6.240/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BCH-EUR — BUILDING_ACCELERATION — score 5.621/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — BUILDING_ACCELERATION — score 5.225/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 9.738/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.767/10 — sources ACCELERATION — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.732/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.364/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SFP-EUR — MEMORY_24H — score mémoire 8.323/10 — sources ACCELERATION — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.070/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.907/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +89.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +68.82% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AIOZ-EUR +54.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZETA-EUR +51.78% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- FORM-EUR +38.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +36.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SWELL-EUR +35.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +34.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUFFER-EUR +24.40% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- SYN-EUR +22.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
