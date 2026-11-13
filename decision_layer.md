# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-13T03:30:24.916367+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : SXT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.697 | entrée 5.200 | trend 7.900 | rang 6.549
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SXT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.549
2. KITE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.485

## Accélération indépendante

- INIT-EUR — CONFIRMED_ACCELERATION — score 6.767/10 — DETECTED_BUT_TOO_LATE
- ARKM-EUR — BUILDING_ACCELERATION — score 5.934/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QNT-EUR — BUILDING_ACCELERATION — score 5.654/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XAN-EUR — BUILDING_ACCELERATION — score 4.981/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WIN-EUR — MEMORY_DECAY_24_72H — score mémoire 9.402/10 — sources ACCELERATION — MEMORY_ONLY
- HUMA-EUR — MEMORY_24H — score mémoire 8.528/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- INIT-EUR — ACTIVE_NOW — score mémoire 6.767/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- SXT-EUR — ACTIVE_NOW — score mémoire 6.549/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 6.485/10 — sources DECISION_LAYER — WATCH_ONLY
- CT-EUR — MEMORY_24H — score mémoire 6.476/10 — sources ACCELERATION — MEMORY_ONLY
- OPEN-EUR — MEMORY_24H — score mémoire 6.406/10 — sources DECISION_LAYER — MEMORY_ONLY
- BEAM-EUR — MEMORY_DECAY_24_72H — score mémoire 6.272/10 — sources DECISION_LAYER — MEMORY_ONLY
- MLN-EUR — MEMORY_DECAY_24_72H — score mémoire 6.136/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- DODO-EUR +20.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +15.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROM-EUR +7.94% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- OSMO-EUR +4.97% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TIA-EUR +4.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +4.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PLUME-EUR +3.95% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- HUMA-EUR +3.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MEGA-EUR +3.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OPEN-EUR +3.05% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
