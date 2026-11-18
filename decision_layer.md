# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-18T20:51:41.316632+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : KITE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.892 | entrée 5.950 | trend 7.650 | rang 6.602
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KITE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.602

## Accélération indépendante

- TOWNS-EUR — CONFIRMED_ACCELERATION — score 9.889/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CPOOL-EUR — CONFIRMED_ACCELERATION — score 8.640/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLMR-EUR — BUILDING_ACCELERATION — score 4.978/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TOWNS-EUR — ACTIVE_NOW — score mémoire 9.889/10 — sources ACCELERATION — WATCH_ONLY
- MMT-EUR — MEMORY_24H — score mémoire 9.871/10 — sources ACCELERATION — MEMORY_ONLY
- CPOOL-EUR — ACTIVE_NOW — score mémoire 8.640/10 — sources ACCELERATION — WATCH_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 7.650/10 — sources ACCELERATION — MEMORY_ONLY
- MEGA-EUR — ACTIVE_NOW — score mémoire 7.165/10 — sources V4 — WATCH_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 7.154/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- HMSTR-EUR — MEMORY_24H — score mémoire 6.740/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 6.679/10 — sources ACCELERATION — MEMORY_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 6.602/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- BREV-EUR — MEMORY_DECAY_24_72H — score mémoire 6.129/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- MMT-EUR +78.60% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +33.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZKC-EUR +25.08% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WHUF-EUR +20.95% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IRYS-EUR +20.83% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZIL-EUR +19.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOON-EUR +19.14% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NES-EUR +17.28% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HUMA-EUR +14.15% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZKP-EUR +10.93% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
