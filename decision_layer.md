# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-22T21:03:34.584332+00:00
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

- NES-EUR — CONFIRMED_ACCELERATION — score 7.064/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — BUILDING_ACCELERATION — score 5.291/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICNT-EUR — BUILDING_ACCELERATION — score 5.062/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZBCN-EUR — MEMORY_24H — score mémoire 7.991/10 — sources ACCELERATION — MEMORY_ONLY
- NPC-EUR — MEMORY_DECAY_24_72H — score mémoire 7.983/10 — sources ACCELERATION — MEMORY_ONLY
- ORCA-EUR — MEMORY_24H — score mémoire 7.601/10 — sources ACCELERATION — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 7.598/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — ACTIVE_NOW — score mémoire 7.064/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- PUFFER-EUR — MEMORY_24H — score mémoire 6.780/10 — sources ACCELERATION — MEMORY_ONLY
- RARE-EUR — MEMORY_24H — score mémoire 6.604/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- VVV-EUR — MEMORY_24H — score mémoire 6.520/10 — sources DECISION_LAYER — MEMORY_ONLY
- DODO-EUR — MEMORY_DECAY_24_72H — score mémoire 6.507/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 6.474/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ELSA-EUR +26.59% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALIGN-EUR +20.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZKJ-EUR +16.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DRV-EUR +9.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VELO-EUR +8.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZBCN-EUR +8.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LISTA-EUR +8.27% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUMP-EUR +8.04% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ETHFI-EUR +7.75% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- VVV-EUR +7.57% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
