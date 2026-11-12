# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-12T17:53:22.552100+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : SXT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.561 | entrée 6.100 | trend 8.650 | rang 7.217
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : OPEN-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.413 | entrée 5.850 | trend 7.750 | rang 6.406
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SXT-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.217
2. OPEN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.406

## Accélération indépendante

- ALIGN-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- CT-EUR — BUILDING_ACCELERATION — score 6.476/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MON-EUR — BUILDING_ACCELERATION — score 5.783/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BAND-EUR — BUILDING_ACCELERATION — score 5.357/10 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — BUILDING_ACCELERATION — score 5.292/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DODO-EUR — BUILDING_ACCELERATION — score 5.070/10 — DETECTED_BUT_TOO_LATE
- MASK-EUR — BUILDING_ACCELERATION — score 4.935/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- WIN-EUR — MEMORY_24H — score mémoire 9.693/10 — sources ACCELERATION — MEMORY_ONLY
- HUMA-EUR — MEMORY_24H — score mémoire 8.528/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- SXT-EUR — ACTIVE_NOW — score mémoire 7.217/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CT-EUR — ACTIVE_NOW — score mémoire 6.476/10 — sources ACCELERATION — WATCH_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 6.466/10 — sources DECISION_LAYER — MEMORY_ONLY
- GRASS-EUR — MEMORY_24H — score mémoire 6.449/10 — sources ACCELERATION — MEMORY_ONLY
- OPEN-EUR — ACTIVE_NOW — score mémoire 6.406/10 — sources DECISION_LAYER — WATCH_ONLY
- MLN-EUR — MEMORY_24H — score mémoire 6.326/10 — sources ACCELERATION — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 6.265/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- DODO-EUR +18.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALIGN-EUR +7.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- XMN-EUR +5.34% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROM-EUR +4.75% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MON-EUR +4.14% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ARX-EUR +3.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PARTI-EUR +3.79% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- OPEN-EUR +3.71% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CTR-EUR +3.36% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CROSS-EUR +3.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
