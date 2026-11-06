# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-06T03:00:12.657942+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ELSA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.603 | entrée 6.200 | trend 7.650 | rang 6.535
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.535
2. TRUST-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.356

## Accélération indépendante

- BIRB-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- TRIA-EUR — CONFIRMED_ACCELERATION — score 9.163/10 — DETECTED_BUT_TOO_LATE
- PTB-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QKC-EUR — CONFIRMED_ACCELERATION — score 6.775/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PORTAL-EUR — BUILDING_ACCELERATION — score 6.136/10 — DETECTED_BUT_TOO_LATE
- HUMA-EUR — BUILDING_ACCELERATION — score 6.069/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RED-EUR — BUILDING_ACCELERATION — score 5.010/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PARTI-EUR — BUILDING_ACCELERATION — score 4.799/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- BIRB-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER — DETECTED_BUT_TOO_LATE
- EDGE-EUR — MEMORY_DECAY_24_72H — score mémoire 9.486/10 — sources ACCELERATION — MEMORY_ONLY
- TRIA-EUR — ACTIVE_NOW — score mémoire 9.163/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ALIGN-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION — MEMORY_ONLY
- PTB-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION — WATCH_ONLY
- ADX-EUR — MEMORY_DECAY_24_72H — score mémoire 8.198/10 — sources ACCELERATION — MEMORY_ONLY
- CHILLGUY-EUR — MEMORY_DECAY_24_72H — score mémoire 8.067/10 — sources ACCELERATION — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.025/10 — sources ACCELERATION — MEMORY_ONLY
- ARX-EUR — MEMORY_24H — score mémoire 7.773/10 — sources ACCELERATION — MEMORY_ONLY
- PUFFER-EUR — MEMORY_DECAY_24_72H — score mémoire 7.771/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- CYBER-EUR +29.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALIGN-EUR +29.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +26.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +11.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- UP-EUR +11.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PARTI-EUR +9.06% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROMPT-EUR +7.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARX-EUR +7.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PTB-EUR +7.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +6.60% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
