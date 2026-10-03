# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T11:12:53.199917+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.621 | entrée 8.050 | trend 8.900 | rang 8.322
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : FLUID-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.006 | entrée 5.900 | trend 9.000 | rang 7.859
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : IMX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.268 | entrée 6.300 | trend 9.200 | rang 8.107
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.322 — opportunité 8.621 — entrée 8.050 — trend 8.900
2. SUI-EUR — ACHETE_MAINTENANT — rank 6.904 — opportunité 7.896 — entrée 7.450 — trend 6.300
3. WIF-EUR — ACHETE_MAINTENANT — rank 6.411 — opportunité 8.438 — entrée 6.850 — trend 4.850
4. RENDER-EUR — ACHETE_MAINTENANT — rank 6.404 — opportunité 7.178 — entrée 7.200 — trend 5.800

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.322
2. IMX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.107
3. FLUID-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.859

## Accélération indépendante

- GLMR-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- UP-EUR — CONFIRMED_ACCELERATION — score 7.325/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 1INCH-EUR — CONFIRMED_ACCELERATION — score 7.175/10 — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — BUILDING_ACCELERATION — score 5.500/10 — DETECTED_BUT_TOO_LATE
- W-EUR — BUILDING_ACCELERATION — score 4.878/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EDGE-EUR — MEMORY_DECAY_24_72H — score mémoire 8.712/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_DECAY_24_72H — score mémoire 8.608/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GLMR-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.322/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 8.107/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.048/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- GLMR-EUR +33.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HFT-EUR +14.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ATH-EUR +13.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAND-EUR +12.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +11.55% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- WLD-EUR +11.41% — DETECTED_EARLY — couche NONE — action NONE
- SUPER-EUR +9.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +8.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +8.52% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GRASS-EUR +7.45% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
