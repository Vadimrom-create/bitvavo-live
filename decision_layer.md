# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-23T09:20:53.652146+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : KITE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.230 | entrée 5.650 | trend 8.500 | rang 7.106
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KITE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.106

## Accélération indépendante

- QNT-EUR — BUILDING_ACCELERATION — score 5.650/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRUST-EUR — BUILDING_ACCELERATION — score 5.358/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DATAIP-EUR — BUILDING_ACCELERATION — score 5.149/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JUP-EUR — BUILDING_ACCELERATION — score 5.121/10 — DETECTED_BUT_TOO_LATE
- ELSA-EUR — BUILDING_ACCELERATION — score 5.093/10 — DETECTED_BUT_TOO_LATE
- ICNT-EUR — BUILDING_ACCELERATION — score 4.913/10 — DETECTED_BUT_TOO_LATE
- CYBER-EUR — BUILDING_ACCELERATION — score 4.762/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZEUS-EUR — MEMORY_24H — score mémoire 7.598/10 — sources ACCELERATION — MEMORY_ONLY
- ZBCN-EUR — MEMORY_DECAY_24_72H — score mémoire 7.499/10 — sources ACCELERATION — MEMORY_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 7.106/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- NES-EUR — MEMORY_24H — score mémoire 7.064/10 — sources ACCELERATION — MEMORY_ONLY
- EPIC-EUR — MEMORY_24H — score mémoire 6.856/10 — sources ACCELERATION — MEMORY_ONLY
- RARE-EUR — MEMORY_24H — score mémoire 6.604/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- VVV-EUR — MEMORY_24H — score mémoire 6.520/10 — sources DECISION_LAYER — MEMORY_ONLY
- CROSS-EUR — MEMORY_24H — score mémoire 6.452/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_DECAY_24_72H — score mémoire 6.362/10 — sources ACCELERATION — MEMORY_ONLY
- ORCA-EUR — MEMORY_DECAY_24_72H — score mémoire 6.135/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ELSA-EUR +28.36% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLUR-EUR +15.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LISTA-EUR +15.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IMU-EUR +14.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- JUP-EUR +12.73% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- DRV-EUR +10.53% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALIGN-EUR +10.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLUX-EUR +9.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- QNT-EUR +8.38% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- DODO-EUR +7.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
