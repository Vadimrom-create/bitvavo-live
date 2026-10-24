# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-24T05:41:11.965752+00:00
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

- RED-EUR — BUILDING_ACCELERATION — score 6.454/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- U-EUR — BUILDING_ACCELERATION — score 5.631/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRIA-EUR — BUILDING_ACCELERATION — score 5.521/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 5.492/10 — DETECTED_BUT_TOO_LATE
- ZORA-EUR — BUILDING_ACCELERATION — score 5.455/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FUEL-EUR — BUILDING_ACCELERATION — score 4.960/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SYN-EUR — MEMORY_24H — score mémoire 8.740/10 — sources ACCELERATION — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.689/10 — sources ACCELERATION — MEMORY_ONLY
- BIRB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- EPIC-EUR — MEMORY_DECAY_24_72H — score mémoire 8.002/10 — sources ACCELERATION — MEMORY_ONLY
- ZEUS-EUR — MEMORY_DECAY_24_72H — score mémoire 7.891/10 — sources ACCELERATION — MEMORY_ONLY
- AXIS-EUR — MEMORY_24H — score mémoire 7.606/10 — sources ACCELERATION — MEMORY_ONLY
- CPOOL-EUR — MEMORY_DECAY_24_72H — score mémoire 7.469/10 — sources ACCELERATION — MEMORY_ONLY
- ELSA-EUR — MEMORY_24H — score mémoire 7.343/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.153/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RECALL-EUR — MEMORY_24H — score mémoire 7.053/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- IRYS-EUR +221.54% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +165.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- UP-EUR +72.42% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- QUID-EUR +32.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +28.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXIS-EUR +24.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +22.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BLEND-EUR +21.84% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CTR-EUR +19.80% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- TREE-EUR +19.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
