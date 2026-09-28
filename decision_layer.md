# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T01:30:16.881557+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : CC-EUR | action ACHETE_MAINTENANT | opportunité 9.092 | entrée 6.800 | trend 8.700 | rang 8.208
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : KAS-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.955 | entrée 5.800 | trend 8.900 | rang 7.799
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BRETT-EUR | action LATENT_ACCELERATOR | opportunité 8.690 | entrée 4.800 | trend 9.000 | rang 8.053
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : EGLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.232 | entrée 5.950 | trend 8.400 | rang 8.225
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. CC-EUR — ACHETE_MAINTENANT — rank 8.208 — opportunité 9.092 — entrée 6.800 — trend 8.700
2. RENDER-EUR — ACHETE_MAINTENANT — rank 8.184 — opportunité 8.087 — entrée 7.600 — trend 9.200
3. ALGO-EUR — ACHETE_MAINTENANT — rank 7.906 — opportunité 8.209 — entrée 7.350 — trend 8.700
4. HBAR-EUR — ACHETE_MAINTENANT — rank 7.843 — opportunité 8.958 — entrée 7.400 — trend 7.700
5. TRX-EUR — ACHETE_MAINTENANT — rank 5.410 — opportunité 6.495 — entrée 7.650 — trend 3.900

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. EGLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.225
2. CC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.208
3. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.184

## Accélération indépendante

- AMP-EUR — CONFIRMED_ACCELERATION — score 8.122/10 — DETECTED_BUT_TOO_LATE
- SOSO-EUR — BUILDING_ACCELERATION — score 5.876/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CC-EUR — ACTIVE_NOW — score mémoire 8.208/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DGB-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QNT-EUR — MEMORY_24H — score mémoire 8.429/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- EGLD-EUR — ACTIVE_NOW — score mémoire 8.225/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.184/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BABY-EUR — ACTIVE_NOW — score mémoire 8.138/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AMP-EUR — ACTIVE_NOW — score mémoire 8.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- QNT-EUR +40.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +32.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INX-EUR +27.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +27.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +25.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +18.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IRYS-EUR +17.77% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PUMP-EUR +17.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMX-EUR +15.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TRUST-EUR +14.12% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
