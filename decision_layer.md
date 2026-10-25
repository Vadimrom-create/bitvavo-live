# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-25T12:32:09.888107+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ELSA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.661 | entrée 5.350 | trend 8.250 | rang 7.099
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.099
2. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.767

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 8.974/10 — DETECTED_BUT_TOO_LATE
- U-EUR — CONFIRMED_ACCELERATION — score 7.794/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IQ-EUR — CONFIRMED_ACCELERATION — score 7.702/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CVC-EUR — CONFIRMED_ACCELERATION — score 6.736/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DOS-EUR — BUILDING_ACCELERATION — score 5.299/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — BUILDING_ACCELERATION — score 5.229/10 — DETECTED_BUT_TOO_LATE
- BABY-EUR — BUILDING_ACCELERATION — score 5.086/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUNDIX-EUR — BUILDING_ACCELERATION — score 4.793/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TREAD-EUR — ACTIVE_NOW — score mémoire 8.974/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- BIRB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- TREE-EUR — MEMORY_DECAY_24_72H — score mémoire 8.178/10 — sources ACCELERATION — MEMORY_ONLY
- CHIP-EUR — MEMORY_24H — score mémoire 7.845/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 7.794/10 — sources ACCELERATION — WATCH_ONLY
- IQ-EUR — ACTIVE_NOW — score mémoire 7.702/10 — sources ACCELERATION — WATCH_ONLY
- 0G-EUR — MEMORY_24H — score mémoire 7.620/10 — sources ACCELERATION — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.452/10 — sources ACCELERATION — MEMORY_ONLY
- USELESS-EUR — MEMORY_24H — score mémoire 7.391/10 — sources ACCELERATION — MEMORY_ONLY
- QKC-EUR — MEMORY_24H — score mémoire 7.336/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- TREAD-EUR +39.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +29.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- T-EUR +19.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CNPY-EUR +12.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- USELESS-EUR +9.59% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- GROVE-EUR +6.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MLN-EUR +6.42% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +6.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CHIP-EUR +5.91% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ARX-EUR +5.78% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
