# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-23T05:30:18.144951+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ELSA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.210 | entrée 4.950 | trend 8.450 | rang 7.013
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.013
2. PROM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.591
3. PHA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.325

## Accélération indépendante

- EPIC-EUR — CONFIRMED_ACCELERATION — score 8.032/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — CONFIRMED_ACCELERATION — score 7.921/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PHA-EUR — CONFIRMED_ACCELERATION — score 6.928/10 — DETECTED_BUT_TOO_LATE
- REZ-EUR — BUILDING_ACCELERATION — score 6.306/10 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — BUILDING_ACCELERATION — score 6.102/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GROVE-EUR — BUILDING_ACCELERATION — score 5.800/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PIXEL-EUR — BUILDING_ACCELERATION — score 5.714/10 — DETECTED_BUT_TOO_LATE
- CSPR-EUR — BUILDING_ACCELERATION — score 5.319/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 8.820/10 — sources ACCELERATION — MEMORY_ONLY
- EPIC-EUR — ACTIVE_NOW — score mémoire 8.032/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — ACTIVE_NOW — score mémoire 7.921/10 — sources ACCELERATION — WATCH_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 7.742/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — MEMORY_24H — score mémoire 7.722/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.699/10 — sources ACCELERATION — MEMORY_ONLY
- ORCA-EUR — MEMORY_DECAY_24_72H — score mémoire 7.355/10 — sources ACCELERATION — MEMORY_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 7.238/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICNT-EUR — MEMORY_24H — score mémoire 7.112/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 7.065/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- IRYS-EUR +25.97% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GROVE-EUR +18.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +13.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OSMO-EUR +13.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +12.36% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DOS-EUR +12.02% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- REZ-EUR +10.84% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- KERNEL-EUR +10.36% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MEW-EUR +10.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +6.67% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
