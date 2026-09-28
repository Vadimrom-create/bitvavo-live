# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T17:43:18.983697+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XDC-EUR | action ACHETE_MAINTENANT | opportunité 9.223 | entrée 7.100 | trend 9.000 | rang 8.361
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MANA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.955 | entrée 6.100 | trend 7.400 | rang 7.077
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AZTEC-EUR | action LATENT_ACCELERATOR | opportunité 7.688 | entrée 5.650 | trend 8.600 | rang 6.973
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MIOTA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.890 | entrée 6.450 | trend 9.200 | rang 8.069
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XDC-EUR — ACHETE_MAINTENANT — rank 8.361 — opportunité 9.223 — entrée 7.100 — trend 9.000
2. CC-EUR — ACHETE_MAINTENANT — rank 7.333 — opportunité 8.852 — entrée 6.850 — trend 6.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XDC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.361
2. MIOTA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.069
3. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.058

## Accélération indépendante

- RUNE-EUR — CONFIRMED_ACCELERATION — score 7.898/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WMTX-EUR — CONFIRMED_ACCELERATION — score 6.734/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 5.701/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XYO-EUR — BUILDING_ACCELERATION — score 5.657/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NMR-EUR — BUILDING_ACCELERATION — score 5.566/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 5.443/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDEN-EUR — BUILDING_ACCELERATION — score 5.296/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GOAT-EUR — BUILDING_ACCELERATION — score 4.909/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MIOTA-EUR — BUILDING_ACCELERATION — score 4.762/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XDC-EUR — ACTIVE_NOW — score mémoire 8.361/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CC-EUR — ACTIVE_NOW — score mémoire 7.333/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- IMU-EUR — MEMORY_24H — score mémoire 9.209/10 — sources ACCELERATION — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RECALL-EUR — MEMORY_24H — score mémoire 8.403/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 8.069/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- RUNE-EUR — ACTIVE_NOW — score mémoire 8.058/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- HBAR-EUR +38.17% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +35.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALGO-EUR +14.81% — DETECTED_EARLY — couche NONE — action NONE
- IKA-EUR +12.72% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- MIOTA-EUR +11.66% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NMR-EUR +9.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +8.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MON-EUR +8.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XDC-EUR +8.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LINK-EUR +7.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
