# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-28T11:11:32.914356+00:00
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

- O-EUR — CONFIRMED_ACCELERATION — score 9.678/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HEI-EUR — BUILDING_ACCELERATION — score 5.526/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INIT-EUR — BUILDING_ACCELERATION — score 5.070/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- O-EUR — ACTIVE_NOW — score mémoire 9.678/10 — sources ACCELERATION, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.282/10 — sources ACCELERATION — MEMORY_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.613/10 — sources ACCELERATION — MEMORY_ONLY
- NOM-EUR — MEMORY_24H — score mémoire 7.461/10 — sources ACCELERATION — MEMORY_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.070/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ELSA-EUR — ACTIVE_NOW — score mémoire 7.006/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DODO-EUR — MEMORY_24H — score mémoire 6.879/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AXIS-EUR — MEMORY_24H — score mémoire 6.826/10 — sources ACCELERATION — MEMORY_ONLY
- VVV-EUR — MEMORY_24H — score mémoire 6.659/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- THE-EUR — MEMORY_24H — score mémoire 6.658/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- NES-EUR +12.59% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RAD-EUR +11.89% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- THE-EUR +11.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SKY-EUR +10.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ELSA-EUR +9.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOSO-EUR +7.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SENT-EUR +6.81% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- DODO-EUR +6.40% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- TLM-EUR +5.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- O-EUR +4.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
