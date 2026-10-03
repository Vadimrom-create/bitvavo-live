# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T08:36:42.706341+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.461 | entrée 7.000 | trend 8.900 | rang 8.104
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : IMX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.578 | entrée 5.950 | trend 9.200 | rang 8.184
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ENJ-EUR | action LATENT_ACCELERATOR | opportunité 7.704 | entrée 5.300 | trend 8.400 | rang 7.324
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FLUID-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.188 | entrée 6.900 | trend 8.950 | rang 8.034
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.104 — opportunité 8.461 — entrée 7.000 — trend 8.900
2. SUPER-EUR — ACHETE_MAINTENANT — rank 7.986 — opportunité 8.370 — entrée 6.950 — trend 8.800
3. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.824 — opportunité 9.066 — entrée 7.450 — trend 7.600
4. UNI-EUR — ACHETE_MAINTENANT — rank 7.219 — opportunité 8.806 — entrée 7.250 — trend 6.350

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. IMX-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.184
2. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.104
3. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.034

## Accélération indépendante

- HFT-EUR — CONFIRMED_ACCELERATION — score 8.388/10 — DETECTED_BUT_TOO_LATE
- RED-EUR — CONFIRMED_ACCELERATION — score 8.100/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — CONFIRMED_ACCELERATION — score 6.898/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XDP-EUR — BUILDING_ACCELERATION — score 6.164/10 — DETECTED_BUT_TOO_LATE
- FOLD-EUR — BUILDING_ACCELERATION — score 5.254/10 — DETECTED_BUT_TOO_LATE
- KITE-EUR — BUILDING_ACCELERATION — score 5.027/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_DECAY_24_72H — score mémoire 9.254/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — ACTIVE_NOW — score mémoire 8.388/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- IMX-EUR — ACTIVE_NOW — score mémoire 8.184/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.104/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 8.100/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FLUID-EUR — ACTIVE_NOW — score mémoire 8.034/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.986/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +16.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +14.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +14.07% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ATH-EUR +10.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XDP-EUR +10.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +7.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKY-EUR +6.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMX-EUR +6.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +5.85% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- UP-EUR +5.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
