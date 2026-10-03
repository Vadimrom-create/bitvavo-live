# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T05:53:30.364785+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 8.782 | entrée 7.400 | trend 9.000 | rang 8.316
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : IMX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.049 | entrée 6.100 | trend 8.900 | rang 7.815
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MAGIC-EUR | action LATENT_ACCELERATOR | opportunité 7.996 | entrée 5.200 | trend 8.650 | rang 7.576
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AXS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.468 | entrée 7.050 | trend 9.000 | rang 8.019
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 8.316 — opportunité 8.782 — entrée 7.400 — trend 9.000

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.316
2. AXS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.019
3. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.884

## Accélération indépendante

- UP-EUR — CONFIRMED_ACCELERATION — score 7.176/10 — DETECTED_BUT_TOO_LATE
- FOLD-EUR — BUILDING_ACCELERATION — score 5.843/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GTC-EUR — BUILDING_ACCELERATION — score 5.445/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — BUILDING_ACCELERATION — score 5.412/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_DECAY_24_72H — score mémoire 9.821/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SYN-EUR — MEMORY_24H — score mémoire 9.039/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.316/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 8.019/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.884/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 7.815/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +68.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +21.80% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ENJ-EUR +15.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +14.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ATH-EUR +11.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APE-EUR +10.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AXS-EUR +10.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SLP-EUR +8.41% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- UP-EUR +8.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PIXEL-EUR +8.40% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
