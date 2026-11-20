# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-20T23:22:37.984004+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.996 | entrée 6.000 | trend 8.150 | rang 6.638
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.638
2. CROSS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.417
3. CTR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.371

## Accélération indépendante

- ADX-EUR — BUILDING_ACCELERATION — score 5.404/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 4.932/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DUSK-EUR — BUILDING_ACCELERATION — score 4.854/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 4.810/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DATAIP-EUR — BUILDING_ACCELERATION — score 4.769/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HUMA-EUR — MEMORY_24H — score mémoire 8.000/10 — sources ACCELERATION — MEMORY_ONLY
- IKA-EUR — MEMORY_24H — score mémoire 7.094/10 — sources ACCELERATION — MEMORY_ONLY
- BOB-EUR — MEMORY_24H — score mémoire 7.070/10 — sources ACCELERATION — MEMORY_ONLY
- CSPR-EUR — MEMORY_DECAY_24_72H — score mémoire 6.801/10 — sources ACCELERATION — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 6.782/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 6.638/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MMT-EUR — MEMORY_24H — score mémoire 6.500/10 — sources ACCELERATION — MEMORY_ONLY
- HMSTR-EUR — MEMORY_24H — score mémoire 6.467/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KITE-EUR — MEMORY_DECAY_24_72H — score mémoire 6.461/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- ICNT-EUR — MEMORY_24H — score mémoire 6.441/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY

## Audit des plus fortes hausses

- ELSA-EUR +19.39% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KERNEL-EUR +17.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CYBER-EUR +12.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DODO-EUR +11.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLUR-EUR +9.88% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AI-EUR +9.06% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +7.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- O-EUR +6.61% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CARV-EUR +6.15% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HMSTR-EUR +6.08% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
