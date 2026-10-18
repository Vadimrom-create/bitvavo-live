# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-18T10:49:49.146509+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TIA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.360 | entrée 6.050 | trend 8.300 | rang 7.128
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. TIA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.128
2. RSR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.959
3. KMNO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.761

## Accélération indépendante

- AMP-EUR — BUILDING_ACCELERATION — score 6.270/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ELSA-EUR — BUILDING_ACCELERATION — score 6.008/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLMR-EUR — BUILDING_ACCELERATION — score 5.463/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AXL-EUR — MEMORY_DECAY_24_72H — score mémoire 8.228/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_DECAY_24_72H — score mémoire 8.191/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GTC-EUR — MEMORY_24H — score mémoire 7.849/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CPOOL-EUR — MEMORY_DECAY_24_72H — score mémoire 7.665/10 — sources ACCELERATION — MEMORY_ONLY
- ALT-EUR — MEMORY_24H — score mémoire 7.202/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WAL-EUR — MEMORY_24H — score mémoire 7.187/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TIA-EUR — ACTIVE_NOW — score mémoire 7.128/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DUSK-EUR — ACTIVE_NOW — score mémoire 7.057/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PROM-EUR — MEMORY_DECAY_24_72H — score mémoire 6.984/10 — sources ACCELERATION — MEMORY_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 6.981/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZEUS-EUR +17.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +17.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +15.44% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GWEI-EUR +10.21% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ELSA-EUR +7.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- OSMO-EUR +7.27% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HBAR-EUR +5.87% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- AMP-EUR +5.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BTT-EUR +5.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +5.09% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
