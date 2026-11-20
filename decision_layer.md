# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-20T08:46:43.476025+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : CROSS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.663 | entrée 5.850 | trend 7.800 | rang 6.534
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CROSS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.534
2. ICNT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.441
3. IRYS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.088

## Accélération indépendante

- IKA-EUR — CONFIRMED_ACCELERATION — score 7.094/10 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — CONFIRMED_ACCELERATION — score 6.782/10 — DETECTED_BUT_TOO_LATE
- MMT-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE
- HMSTR-EUR — BUILDING_ACCELERATION — score 6.467/10 — DETECTED_BUT_TOO_LATE
- CROSS-EUR — BUILDING_ACCELERATION — score 5.759/10 — DETECTED_BUT_TOO_LATE
- 2Z-EUR — BUILDING_ACCELERATION — score 5.627/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RUNE-EUR — BUILDING_ACCELERATION — score 5.364/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INIT-EUR — BUILDING_ACCELERATION — score 4.887/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HUMA-EUR — MEMORY_24H — score mémoire 8.000/10 — sources ACCELERATION — MEMORY_ONLY
- ADX-EUR — MEMORY_24H — score mémoire 7.477/10 — sources ACCELERATION — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.456/10 — sources ACCELERATION — MEMORY_ONLY
- TOWNS-EUR — MEMORY_DECAY_24_72H — score mémoire 7.434/10 — sources ACCELERATION — MEMORY_ONLY
- MEGA-EUR — MEMORY_24H — score mémoire 7.238/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- IKA-EUR — ACTIVE_NOW — score mémoire 7.094/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- KITE-EUR — MEMORY_24H — score mémoire 7.083/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- BOB-EUR — MEMORY_24H — score mémoire 7.070/10 — sources ACCELERATION — MEMORY_ONLY
- DYDX-EUR — ACTIVE_NOW — score mémoire 6.782/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- TREAD-EUR — MEMORY_24H — score mémoire 6.641/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- IKA-EUR +64.06% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CYBER-EUR +50.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MMT-EUR +26.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +14.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DOS-EUR +14.62% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CAP-EUR +13.36% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +12.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +12.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- YB-EUR +11.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HUMA-EUR +11.39% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
