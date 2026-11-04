# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-04T16:18:20.160038+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BIRB-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.745 | entrée 6.800 | trend 7.650 | rang 6.633
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BIRB-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.633
2. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.538

## Accélération indépendante

- PUFFER-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- KMNO-EUR — CONFIRMED_ACCELERATION — score 8.560/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — CONFIRMED_ACCELERATION — score 7.864/10 — DETECTED_BUT_TOO_LATE
- VVV-EUR — BUILDING_ACCELERATION — score 6.137/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ADX-EUR — BUILDING_ACCELERATION — score 6.088/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CPOOL-EUR — BUILDING_ACCELERATION — score 5.779/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STX-EUR — BUILDING_ACCELERATION — score 5.693/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DUSK-EUR — BUILDING_ACCELERATION — score 4.787/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PUFFER-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- RUNE-EUR — MEMORY_DECAY_24_72H — score mémoire 9.215/10 — sources ACCELERATION — MEMORY_ONLY
- AXIS-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 8.560/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- NOS-EUR — ACTIVE_NOW — score mémoire 7.864/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ALIGN-EUR — MEMORY_24H — score mémoire 6.724/10 — sources ACCELERATION — MEMORY_ONLY
- BIRB-EUR — ACTIVE_NOW — score mémoire 6.633/10 — sources ACCELERATION, DECISION_LAYER — WATCH_ONLY
- 2Z-EUR — MEMORY_24H — score mémoire 6.578/10 — sources ACCELERATION — MEMORY_ONLY
- PARTI-EUR — MEMORY_24H — score mémoire 6.565/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 6.538/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PTB-EUR +55.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARX-EUR +28.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +26.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ELSA-EUR +18.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOS-EUR +16.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- USELESS-EUR +15.11% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NPC-EUR +15.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DRV-EUR +14.22% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SXT-EUR +12.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLUID-EUR +12.61% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
