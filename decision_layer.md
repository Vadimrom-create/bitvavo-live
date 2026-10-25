# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-25T23:40:46.257733+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : ELSA-EUR | action LATENT_ACCELERATOR | opportunité 7.935 | entrée 5.300 | trend 8.650 | rang 7.497
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : INIT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.510 | entrée 4.750 | trend 8.850 | rang 7.331
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ELSA-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.497
2. INIT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.331
3. AVA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.018

## Accélération indépendante

- PROMPT-EUR — CONFIRMED_ACCELERATION — score 8.192/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — BUILDING_ACCELERATION — score 6.391/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- U-EUR — BUILDING_ACCELERATION — score 6.374/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GTC-EUR — BUILDING_ACCELERATION — score 6.043/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DODO-EUR — BUILDING_ACCELERATION — score 4.776/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 8.974/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 8.890/10 — sources ACCELERATION — MEMORY_ONLY
- BIRB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- PROMPT-EUR — ACTIVE_NOW — score mémoire 8.192/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- IQ-EUR — MEMORY_24H — score mémoire 7.702/10 — sources ACCELERATION — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 7.596/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BABY-EUR — MEMORY_24H — score mémoire 7.580/10 — sources ACCELERATION — MEMORY_ONLY
- ELSA-EUR — ACTIVE_NOW — score mémoire 7.497/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.452/10 — sources ACCELERATION — MEMORY_ONLY
- USELESS-EUR — MEMORY_24H — score mémoire 7.391/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- CAP-EUR +39.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +29.11% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DODO-EUR +17.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- T-EUR +16.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- REZ-EUR +11.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OSMO-EUR +10.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- U-EUR +9.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALIGN-EUR +8.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CNPY-EUR +7.95% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +7.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
