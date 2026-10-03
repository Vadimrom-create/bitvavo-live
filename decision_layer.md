# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T10:16:08.916538+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 9.399 | entrée 7.250 | trend 8.700 | rang 8.217
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : IMX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.556 | entrée 5.900 | trend 9.200 | rang 8.149
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : INIT-EUR | action LATENT_ACCELERATOR | opportunité 7.821 | entrée 5.550 | trend 8.900 | rang 7.673
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GALA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.263 | entrée 6.800 | trend 8.650 | rang 7.944
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 8.217 — opportunité 9.399 — entrée 7.250 — trend 8.700
2. AAVE-EUR — ACHETE_MAINTENANT — rank 8.058 — opportunité 8.386 — entrée 7.000 — trend 8.900
3. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.691 — opportunité 8.692 — entrée 7.000 — trend 7.600
4. RENDER-EUR — ACHETE_MAINTENANT — rank 7.354 — opportunité 8.829 — entrée 7.450 — trend 6.550
5. SUI-EUR — ACHETE_MAINTENANT — rank 7.112 — opportunité 8.415 — entrée 7.250 — trend 6.300
6. ONDO-EUR — ACHETE_MAINTENANT — rank 6.999 — opportunité 8.707 — entrée 7.500 — trend 5.900
7. FET-EUR — ACHETE_MAINTENANT — rank 6.959 — opportunité 8.743 — entrée 7.650 — trend 5.850
8. AVAX-EUR — ACHETE_MAINTENANT — rank 6.780 — opportunité 8.058 — entrée 7.450 — trend 6.050

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.217
2. IMX-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.149
3. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.058

## Accélération indépendante

- WLD-EUR — CONFIRMED_ACCELERATION — score 8.366/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CPOOL-EUR — CONFIRMED_ACCELERATION — score 7.310/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JTO-EUR — BUILDING_ACCELERATION — score 6.362/10 — DETECTED_BUT_TOO_LATE
- ZKJ-EUR — BUILDING_ACCELERATION — score 6.020/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — BUILDING_ACCELERATION — score 5.245/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — BUILDING_ACCELERATION — score 5.161/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 5.142/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MON-EUR — BUILDING_ACCELERATION — score 5.122/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FET-EUR — BUILDING_ACCELERATION — score 4.767/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WLD-EUR — ACTIVE_NOW — score mémoire 8.366/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- FET-EUR — ACTIVE_NOW — score mémoire 6.959/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EDGE-EUR — MEMORY_DECAY_24_72H — score mémoire 8.909/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_DECAY_24_72H — score mémoire 8.786/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 8.149/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.058/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.048/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAND-EUR +22.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HFT-EUR +15.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ATH-EUR +14.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +12.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +12.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +11.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +11.06% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- WLD-EUR +9.12% — DETECTED_EARLY — couche NONE — action NONE
- GRASS-EUR +8.66% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- AGI-EUR +8.11% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
