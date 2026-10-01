# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T03:42:08.459164+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AVAX-EUR | action ACHETE_MAINTENANT | opportunité 8.891 | entrée 7.450 | trend 8.700 | rang 8.245
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AVNT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.125 | entrée 6.150 | trend 8.450 | rang 7.694
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : HUMA-EUR | action LATENT_ACCELERATOR | opportunité 7.850 | entrée 5.550 | trend 8.900 | rang 7.679
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.444 | entrée 6.600 | trend 8.700 | rang 7.883
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AVAX-EUR — ACHETE_MAINTENANT — rank 8.245 — opportunité 8.891 — entrée 7.450 — trend 8.700
2. ALGO-EUR — ACHETE_MAINTENANT — rank 8.166 — opportunité 9.294 — entrée 6.900 — trend 8.400
3. DOT-EUR — ACHETE_MAINTENANT — rank 7.784 — opportunité 8.242 — entrée 7.050 — trend 8.450
4. DOGE-EUR — ACHETE_MAINTENANT — rank 7.094 — opportunité 8.638 — entrée 7.400 — trend 5.600

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AVAX-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.245
2. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.166
3. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.883

## Accélération indépendante

- GLMR-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- ZETA-EUR — CONFIRMED_ACCELERATION — score 7.727/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARK-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — CONFIRMED_ACCELERATION — score 6.971/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 6.562/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WCT-EUR — BUILDING_ACCELERATION — score 6.162/10 — DETECTED_BUT_TOO_LATE
- VANA-EUR — BUILDING_ACCELERATION — score 6.154/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — BUILDING_ACCELERATION — score 6.139/10 — DETECTED_BUT_TOO_LATE
- CHILLGUY-EUR — BUILDING_ACCELERATION — score 6.046/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XDC-EUR — BUILDING_ACCELERATION — score 5.966/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ALGO-EUR — ACTIVE_NOW — score mémoire 8.166/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- LMWR-EUR — MEMORY_24H — score mémoire 9.685/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 9.156/10 — sources ACCELERATION — MEMORY_ONLY
- LIGHTER-EUR — MEMORY_24H — score mémoire 9.020/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 8.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GLMR-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 8.245/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +89.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +45.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +35.89% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TRAC-EUR +24.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STX-EUR +22.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MON-EUR +21.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +19.07% — DETECTED_EARLY — couche NONE — action NONE
- SOON-EUR +16.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +16.40% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ESP-EUR +13.65% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
