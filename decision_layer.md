# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-30T19:44:19.265583+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : PEPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.019 | entrée 7.400 | trend 8.000 | rang 6.997
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PEPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.997
2. INIT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.887
3. HAEDAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.551

## Accélération indépendante

- INIT-EUR — BUILDING_ACCELERATION — score 6.402/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BIRB-EUR — BUILDING_ACCELERATION — score 5.994/10 — DETECTED_BUT_TOO_LATE
- OP-EUR — BUILDING_ACCELERATION — score 5.765/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WCT-EUR — BUILDING_ACCELERATION — score 5.482/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CC-EUR — BUILDING_ACCELERATION — score 5.018/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GWEI-EUR — MEMORY_24H — score mémoire 8.661/10 — sources ACCELERATION — MEMORY_ONLY
- TRX-EUR — MEMORY_24H — score mémoire 8.541/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_DECAY_24_72H — score mémoire 7.747/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 7.500/10 — sources ACCELERATION — MEMORY_ONLY
- GROVE-EUR — MEMORY_DECAY_24_72H — score mémoire 7.437/10 — sources ACCELERATION — MEMORY_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 6.997/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 6.906/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- INIT-EUR — ACTIVE_NOW — score mémoire 6.887/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICNT-EUR — MEMORY_24H — score mémoire 6.884/10 — sources ACCELERATION — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 6.844/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- BIRB-EUR +38.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BEAM-EUR +35.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLUR-EUR +19.54% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KERNEL-EUR +11.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOLV-EUR +9.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GWEI-EUR +8.98% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUNDIX-EUR +8.59% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +8.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DOS-EUR +7.78% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CNPY-EUR +7.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
