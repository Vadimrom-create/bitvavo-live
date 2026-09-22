# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T07:41:30.329907+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PORTAL-EUR | action ACHETE_MAINTENANT | opportunité 8.678 | entrée 6.950 | trend 7.150 | rang 7.215
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SSV-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.780 | entrée 6.200 | trend 8.400 | rang 7.555
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : WAL-EUR | action LATENT_ACCELERATOR | opportunité 7.432 | entrée 4.500 | trend 8.350 | rang 7.188
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ALGO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.210 | entrée 6.600 | trend 8.150 | rang 8.147
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.147
2. MANA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.912
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.905

## Accélération indépendante

- KERNEL-EUR — CONFIRMED_ACCELERATION — score 9.810/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — CONFIRMED_ACCELERATION — score 7.162/10 — DETECTED_BUT_TOO_LATE
- ZKJ-EUR — BUILDING_ACCELERATION — score 6.467/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CYBER-EUR — BUILDING_ACCELERATION — score 5.380/10 — DETECTED_BUT_TOO_LATE
- FLUX-EUR — BUILDING_ACCELERATION — score 5.163/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- KERNEL-EUR — ACTIVE_NOW — score mémoire 9.810/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PHA-EUR — MEMORY_24H — score mémoire 9.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 8.979/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MEW-EUR — MEMORY_24H — score mémoire 8.523/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.147/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.098/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ICX-EUR +103.19% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +100.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +46.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +44.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +29.18% — DETECTED_EARLY — couche NONE — action NONE
- WIF-EUR +24.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +22.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +20.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +19.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FARTCOIN-EUR +18.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
