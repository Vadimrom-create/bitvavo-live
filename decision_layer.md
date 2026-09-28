# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T08:16:25.522322+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : GRAM-EUR | action ACHETE_MAINTENANT | opportunité 8.365 | entrée 7.200 | trend 8.200 | rang 7.774
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SKY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.525 | entrée 6.000 | trend 8.750 | rang 7.572
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : NMR-EUR | action LATENT_ACCELERATOR | opportunité 8.789 | entrée 4.800 | trend 7.900 | rang 7.703
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.219 | entrée 7.150 | trend 8.650 | rang 7.993
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. GRAM-EUR — ACHETE_MAINTENANT — rank 7.774 — opportunité 8.365 — entrée 7.200 — trend 8.200
2. XDC-EUR — ACHETE_MAINTENANT — rank 7.589 — opportunité 8.470 — entrée 7.000 — trend 8.500

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.993
2. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.946
3. VIRTUAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.809

## Accélération indépendante

- HUMA-EUR — CONFIRMED_ACCELERATION — score 8.032/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HBAR-EUR — CONFIRMED_ACCELERATION — score 7.131/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYN-EUR — CONFIRMED_ACCELERATION — score 6.606/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRASS-EUR — BUILDING_ACCELERATION — score 6.004/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — BUILDING_ACCELERATION — score 5.933/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 5.822/10 — DETECTED_BUT_TOO_LATE
- SOSO-EUR — BUILDING_ACCELERATION — score 5.262/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CELR-EUR — BUILDING_ACCELERATION — score 5.141/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XDC-EUR — BUILDING_ACCELERATION — score 5.122/10 — DETECTED_BUT_TOO_LATE
- VELO-EUR — BUILDING_ACCELERATION — score 5.111/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GRAM-EUR — ACTIVE_NOW — score mémoire 7.774/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DGB-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.447/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.187/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 8.032/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.993/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +53.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +37.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AUDIO-EUR +18.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRT-EUR +15.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XDC-EUR +11.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +10.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AZTEC-EUR +9.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +8.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOSO-EUR +8.02% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- SEI-EUR +7.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
