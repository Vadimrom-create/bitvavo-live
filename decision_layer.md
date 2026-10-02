# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T07:55:38.862752+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PUMP-EUR | action ACHETE_MAINTENANT | opportunité 8.581 | entrée 7.550 | trend 8.250 | rang 7.737
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZRO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.737 | entrée 6.450 | trend 8.800 | rang 7.426
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DYDX-EUR | action LATENT_ACCELERATOR | opportunité 8.798 | entrée 5.550 | trend 8.950 | rang 8.103
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.432 | entrée 7.850 | trend 8.900 | rang 7.899
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. PUMP-EUR — ACHETE_MAINTENANT — rank 7.737 — opportunité 8.581 — entrée 7.550 — trend 8.250
2. DOT-EUR — ACHETE_MAINTENANT — rank 7.289 — opportunité 8.790 — entrée 7.200 — trend 6.550
3. BABY-EUR — ACHETE_MAINTENANT — rank 7.157 — opportunité 8.753 — entrée 6.850 — trend 6.450

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DYDX-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 8.103
2. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.899
3. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.762

## Accélération indépendante

- MANA-EUR — CONFIRMED_ACCELERATION — score 8.892/10 — DETECTED_BUT_TOO_LATE
- YGG-EUR — CONFIRMED_ACCELERATION — score 8.005/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GMT-EUR — CONFIRMED_ACCELERATION — score 7.417/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RON-EUR — BUILDING_ACCELERATION — score 5.841/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SIGN-EUR — BUILDING_ACCELERATION — score 5.830/10 — DETECTED_BUT_TOO_LATE
- COTI-EUR — BUILDING_ACCELERATION — score 5.795/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — BUILDING_ACCELERATION — score 5.672/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAND-EUR — BUILDING_ACCELERATION — score 5.432/10 — DETECTED_BUT_TOO_LATE
- FLOCK-EUR — BUILDING_ACCELERATION — score 5.192/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWEAT-EUR — BUILDING_ACCELERATION — score 5.179/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HUMA-EUR — MEMORY_24H — score mémoire 9.205/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OPEN-EUR — MEMORY_24H — score mémoire 9.112/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MANA-EUR — ACTIVE_NOW — score mémoire 8.892/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICX-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.257/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — ACTIVE_NOW — score mémoire 8.103/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.078/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +157.63% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CT-EUR +44.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAND-EUR +38.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +32.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SCR-EUR +15.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +15.21% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AAVE-EUR +11.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZK-EUR +11.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +11.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +11.19% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
