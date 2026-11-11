# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-11T20:15:19.922534+00:00
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

- GRASS-EUR — BUILDING_ACCELERATION — score 6.449/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EPIC-EUR — BUILDING_ACCELERATION — score 5.607/10 — DETECTED_BUT_TOO_LATE
- HUMA-EUR — BUILDING_ACCELERATION — score 5.544/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBT-EUR — BUILDING_ACCELERATION — score 5.308/10 — DETECTED_BUT_TOO_LATE
- STRAX-EUR — BUILDING_ACCELERATION — score 4.974/10 — DETECTED_BUT_TOO_LATE
- HAEDAL-EUR — BUILDING_ACCELERATION — score 4.772/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CNPY-EUR — BUILDING_ACCELERATION — score 4.753/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- THQ-EUR — MEMORY_DECAY_24_72H — score mémoire 9.163/10 — sources ACCELERATION — MEMORY_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- MERL-EUR — MEMORY_DECAY_24_72H — score mémoire 8.999/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- FOLD-EUR — MEMORY_24H — score mémoire 7.719/10 — sources ACCELERATION — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 7.235/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CYBER-EUR — MEMORY_DECAY_24_72H — score mémoire 7.035/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 6.872/10 — sources ACCELERATION — MEMORY_ONLY
- CELR-EUR — MEMORY_DECAY_24_72H — score mémoire 6.790/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_DECAY_24_72H — score mémoire 6.636/10 — sources ACCELERATION — MEMORY_ONLY
- GRASS-EUR — ACTIVE_NOW — score mémoire 6.449/10 — sources ACCELERATION — WATCH_ONLY

## Audit des plus fortes hausses

- EPIC-EUR +12.25% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NPC-EUR +11.44% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +11.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +10.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRO-EUR +10.37% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- TAI-EUR +9.93% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRAM-EUR +9.06% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SPX-EUR +8.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SXT-EUR +7.58% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- DOS-EUR +7.52% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
