# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-11T05:16:50.969479+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : W-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.533 | entrée 6.250 | trend 8.500 | rang 7.205
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZK-EUR | action LATENT_ACCELERATOR | opportunité 7.807 | entrée 5.450 | trend 8.950 | rang 7.052
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CTSI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.489 | entrée 5.750 | trend 8.650 | rang 7.224
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CTSI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.224
2. W-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.205
3. S-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.166

## Accélération indépendante

- S-EUR — CONFIRMED_ACCELERATION — score 6.813/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IO-EUR — BUILDING_ACCELERATION — score 6.088/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BAT-EUR — BUILDING_ACCELERATION — score 5.757/10 — DETECTED_BUT_TOO_LATE
- NEO-EUR — BUILDING_ACCELERATION — score 5.328/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARPA-EUR — BUILDING_ACCELERATION — score 4.964/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DGB-EUR — BUILDING_ACCELERATION — score 4.907/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GTC-EUR — MEMORY_24H — score mémoire 9.580/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.918/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BRETT-EUR — MEMORY_24H — score mémoire 8.610/10 — sources ACCELERATION — MEMORY_ONLY
- LRC-EUR — MEMORY_24H — score mémoire 8.600/10 — sources ACCELERATION — MEMORY_ONLY
- O-EUR — MEMORY_DECAY_24_72H — score mémoire 7.689/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 7.370/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DUSK-EUR — MEMORY_24H — score mémoire 7.292/10 — sources ACCELERATION — MEMORY_ONLY
- APT-EUR — MEMORY_24H — score mémoire 7.265/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAY-EUR — MEMORY_24H — score mémoire 7.242/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTSI-EUR — ACTIVE_NOW — score mémoire 7.224/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LUMIA-EUR +82.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +50.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TIA-EUR +24.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CHIP-EUR +19.28% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AERO-EUR +15.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DOS-EUR +14.21% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZK-EUR +13.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- S-EUR +9.73% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AZTEC-EUR +9.55% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ARX-EUR +9.05% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
