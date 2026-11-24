# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-24T16:35:15.808925+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : KITE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.177 | entrée 6.250 | trend 8.300 | rang 6.928
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KITE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.928

## Accélération indépendante

- LISTA-EUR — CONFIRMED_ACCELERATION — score 7.747/10 — DETECTED_BUT_TOO_LATE
- NES-EUR — CONFIRMED_ACCELERATION — score 6.806/10 — DETECTED_BUT_TOO_LATE
- SKY-EUR — BUILDING_ACCELERATION — score 5.906/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CRO-EUR — BUILDING_ACCELERATION — score 5.424/10 — DETECTED_BUT_TOO_LATE
- ZIG-EUR — BUILDING_ACCELERATION — score 5.394/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SHELL-EUR — BUILDING_ACCELERATION — score 4.915/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- MMT-EUR — MEMORY_24H — score mémoire 9.836/10 — sources ACCELERATION — MEMORY_ONLY
- INIT-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION — MEMORY_ONLY
- LISTA-EUR — ACTIVE_NOW — score mémoire 7.747/10 — sources ACCELERATION, DECISION_LAYER — DETECTED_BUT_TOO_LATE
- DODO-EUR — ACTIVE_NOW — score mémoire 7.095/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 6.928/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 6.918/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — ACTIVE_NOW — score mémoire 6.806/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- VVV-EUR — MEMORY_24H — score mémoire 6.536/10 — sources DECISION_LAYER — MEMORY_ONLY
- FIDA-EUR — MEMORY_24H — score mémoire 6.234/10 — sources ACCELERATION — MEMORY_ONLY
- SOMI-EUR — MEMORY_24H — score mémoire 6.201/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- LISTA-EUR +26.83% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MMT-EUR +16.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +12.39% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +12.33% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RPL-EUR +6.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DODO-EUR +6.48% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- INX-EUR +5.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRC-EUR +5.66% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LUNA-EUR +4.13% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- BABY-EUR +3.98% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
