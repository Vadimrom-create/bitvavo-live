# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T00:27:48.225988+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 9.341 | entrée 7.700 | trend 8.450 | rang 8.189
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : HUMA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.129 | entrée 5.950 | trend 8.850 | rang 7.808
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : FLUID-EUR | action LATENT_ACCELERATOR | opportunité 7.976 | entrée 5.500 | trend 8.800 | rang 7.662
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : STX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.338 | entrée 6.750 | trend 8.650 | rang 7.865
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 8.189 — opportunité 9.341 — entrée 7.700 — trend 8.450
2. LTC-EUR — ACHETE_MAINTENANT — rank 7.298 — opportunité 8.868 — entrée 7.700 — trend 6.600
3. RENDER-EUR — ACHETE_MAINTENANT — rank 7.084 — opportunité 8.620 — entrée 6.900 — trend 6.550
4. SUI-EUR — ACHETE_MAINTENANT — rank 6.972 — opportunité 8.767 — entrée 7.600 — trend 5.900
5. GMT-EUR — ACHETE_MAINTENANT — rank 6.650 — opportunité 8.214 — entrée 7.200 — trend 5.900
6. ADA-EUR — ACHETE_MAINTENANT — rank 6.638 — opportunité 8.034 — entrée 7.600 — trend 5.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.189
2. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.865
3. SKY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.829

## Accélération indépendante

- FOLD-EUR — CONFIRMED_ACCELERATION — score 9.866/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EPIC-EUR — CONFIRMED_ACCELERATION — score 7.658/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BLUR-EUR — CONFIRMED_ACCELERATION — score 7.050/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — CONFIRMED_ACCELERATION — score 6.978/10 — DETECTED_BUT_TOO_LATE
- TOSHI-EUR — CONFIRMED_ACCELERATION — score 6.870/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SUI-EUR — BUILDING_ACCELERATION — score 5.791/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ATH-EUR — BUILDING_ACCELERATION — score 5.777/10 — DETECTED_BUT_TOO_LATE
- KITE-EUR — BUILDING_ACCELERATION — score 5.454/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- THQ-EUR — BUILDING_ACCELERATION — score 5.059/10 — DETECTED_BUT_TOO_LATE
- NPC-EUR — BUILDING_ACCELERATION — score 5.020/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SUI-EUR — ACTIVE_NOW — score mémoire 6.972/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FOLD-EUR — ACTIVE_NOW — score mémoire 9.866/10 — sources ACCELERATION, V4 — WATCH_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.189/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- C-EUR — ACTIVE_NOW — score mémoire 8.012/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BILL-EUR — MEMORY_24H — score mémoire 7.878/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAND-EUR +47.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ATH-EUR +17.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +16.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- APE-EUR +11.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENJ-EUR +11.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SPK-EUR +10.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WLD-EUR +10.27% — DETECTED_EARLY — couche NONE — action NONE
- MANA-EUR +9.98% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AXS-EUR +7.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEW-EUR +7.28% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
