# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-24T23:51:17.008235+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ELSA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.534 | entrée 5.900 | trend 8.600 | rang 7.276
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : INIT-EUR | action LATENT_ACCELERATOR | opportunité 7.689 | entrée 5.150 | trend 8.600 | rang 7.052
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.220 | entrée 6.200 | trend 8.050 | rang 6.941
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ELSA-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.276
2. INIT-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.052
3. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.941

## Accélération indépendante

- BIRB-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- CSPR-EUR — CONFIRMED_ACCELERATION — score 7.452/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — CONFIRMED_ACCELERATION — score 7.391/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CT-EUR — CONFIRMED_ACCELERATION — score 7.269/10 — DETECTED_BUT_TOO_LATE
- GRASS-EUR — BUILDING_ACCELERATION — score 6.363/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PYTH-EUR — BUILDING_ACCELERATION — score 5.882/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KITE-EUR — BUILDING_ACCELERATION — score 5.712/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 5.600/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ENA-EUR — BUILDING_ACCELERATION — score 5.492/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CAP-EUR — BUILDING_ACCELERATION — score 5.461/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EPIC-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 9.557/10 — sources ACCELERATION — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.689/10 — sources ACCELERATION — MEMORY_ONLY
- TREE-EUR — MEMORY_24H — score mémoire 8.663/10 — sources ACCELERATION — MEMORY_ONLY
- BIRB-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- SYN-EUR — MEMORY_DECAY_24_72H — score mémoire 7.961/10 — sources ACCELERATION — MEMORY_ONLY
- CHIP-EUR — MEMORY_24H — score mémoire 7.845/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.754/10 — sources ACCELERATION — MEMORY_ONLY
- 0G-EUR — MEMORY_24H — score mémoire 7.620/10 — sources ACCELERATION — MEMORY_ONLY
- BREV-EUR — MEMORY_24H — score mémoire 7.538/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- EPIC-EUR +33.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ANIME-EUR +27.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- UP-EUR +22.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NIL-EUR +14.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +14.09% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +12.43% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZORA-EUR +9.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICNT-EUR +9.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROMPT-EUR +9.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- REZ-EUR +9.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
