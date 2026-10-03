# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T17:04:54.231366+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : INIT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.711 | entrée 6.450 | trend 8.500 | rang 7.333
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 7.561 | entrée 5.200 | trend 8.650 | rang 7.276
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.194 | entrée 6.900 | trend 9.200 | rang 7.969
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.969
2. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.496
3. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.463

## Accélération indépendante

- STRK-EUR — CONFIRMED_ACCELERATION — score 7.386/10 — DETECTED_BUT_TOO_LATE
- MON-EUR — BUILDING_ACCELERATION — score 5.796/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BONK-EUR — BUILDING_ACCELERATION — score 5.504/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GTC-EUR — BUILDING_ACCELERATION — score 5.090/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FOLD-EUR — BUILDING_ACCELERATION — score 4.958/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.048/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.969/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 7.645/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 7.622/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 7.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BAT-EUR — MEMORY_24H — score mémoire 7.532/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- GLMR-EUR +40.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +25.42% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +15.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAND-EUR +14.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +13.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HFT-EUR +12.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZAMA-EUR +11.53% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- XDP-EUR +10.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FUN-EUR +10.33% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +8.39% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
