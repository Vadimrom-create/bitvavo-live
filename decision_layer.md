# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-12T09:44:44.848989+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
Aucun candidat ne remplit actuellement un bucket décisionnel.

## Accélération indépendante

- HUMA-EUR — CONFIRMED_ACCELERATION — score 8.528/10 — DETECTED_BUT_TOO_LATE
- MON-EUR — CONFIRMED_ACCELERATION — score 7.383/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 5.638/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EPIC-EUR — BUILDING_ACCELERATION — score 5.554/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NES-EUR — BUILDING_ACCELERATION — score 5.436/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — BUILDING_ACCELERATION — score 5.110/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WIN-EUR — MEMORY_24H — score mémoire 9.693/10 — sources ACCELERATION — MEMORY_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 8.528/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- MON-EUR — ACTIVE_NOW — score mémoire 7.383/10 — sources ACCELERATION — WATCH_ONLY
- CPOOL-EUR — MEMORY_DECAY_24_72H — score mémoire 7.195/10 — sources ACCELERATION — MEMORY_ONLY
- THQ-EUR — MEMORY_DECAY_24_72H — score mémoire 6.522/10 — sources ACCELERATION — MEMORY_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 6.466/10 — sources DECISION_LAYER — MEMORY_ONLY
- GRASS-EUR — MEMORY_24H — score mémoire 6.449/10 — sources ACCELERATION — MEMORY_ONLY
- NPC-EUR — MEMORY_24H — score mémoire 6.431/10 — sources ACCELERATION — MEMORY_ONLY
- MERL-EUR — MEMORY_DECAY_24_72H — score mémoire 6.406/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- MLN-EUR — MEMORY_24H — score mémoire 6.326/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- TREAD-EUR +17.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EPIC-EUR +10.97% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SXT-EUR +8.53% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- HAEDAL-EUR +7.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PARTI-EUR +7.05% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ARX-EUR +6.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CROSS-EUR +6.44% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WIN-EUR +6.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRAM-EUR +6.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CT-EUR +5.50% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
