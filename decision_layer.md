# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T01:36:44.125592+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : DOT-EUR | action ACHETE_MAINTENANT | opportunité 9.235 | entrée 8.050 | trend 8.250 | rang 8.415
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : COW-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.203 | entrée 5.800 | trend 8.900 | rang 7.890
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SUSHI-EUR | action LATENT_ACCELERATOR | opportunité 8.987 | entrée 5.500 | trend 7.400 | rang 7.518
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.796 | entrée 6.750 | trend 9.200 | rang 8.318
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DOT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.415
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.318
3. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.240

## Accélération indépendante

- THE-EUR — CONFIRMED_ACCELERATION — score 8.475/10 — DETECTED_BUT_TOO_LATE
- AVNT-EUR — CONFIRMED_ACCELERATION — score 7.959/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CPOOL-EUR — CONFIRMED_ACCELERATION — score 7.904/10 — DETECTED_BUT_TOO_LATE
- PUMP-EUR — CONFIRMED_ACCELERATION — score 7.862/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEWT-EUR — CONFIRMED_ACCELERATION — score 7.223/10 — DETECTED_BUT_TOO_LATE
- TREE-EUR — CONFIRMED_ACCELERATION — score 7.106/10 — DETECTED_BUT_TOO_LATE
- CARV-EUR — CONFIRMED_ACCELERATION — score 7.082/10 — DETECTED_BUT_TOO_LATE
- U-EUR — CONFIRMED_ACCELERATION — score 6.626/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SPK-EUR — BUILDING_ACCELERATION — score 6.183/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 6.064/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PUMP-EUR — ACTIVE_NOW — score mémoire 7.862/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GIGA-EUR — MEMORY_24H — score mémoire 9.738/10 — sources ACCELERATION — MEMORY_ONLY
- BOB-EUR — MEMORY_24H — score mémoire 9.007/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.732/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- THE-EUR — ACTIVE_NOW — score mémoire 8.475/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 8.415/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +82.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +74.01% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- KERNEL-EUR +59.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZETA-EUR +50.83% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- AIOZ-EUR +41.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +34.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +32.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CPOOL-EUR +28.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEPE-EUR +24.77% — DETECTED_EARLY — couche NONE — action NONE
- WIF-EUR +23.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
