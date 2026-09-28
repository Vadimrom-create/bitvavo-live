# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T17:58:59.289880+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XDC-EUR | action ACHETE_MAINTENANT | opportunité 9.052 | entrée 7.450 | trend 9.000 | rang 8.365
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SEI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.642 | entrée 6.000 | trend 8.600 | rang 7.274
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : MAGIC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.076 | entrée 6.500 | trend 7.700 | rang 7.829
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XDC-EUR — ACHETE_MAINTENANT — rank 8.365 — opportunité 9.052 — entrée 7.450 — trend 9.000
2. CC-EUR — ACHETE_MAINTENANT — rank 7.112 — opportunité 8.600 — entrée 6.850 — trend 6.650
3. SYRUP-EUR — ACHETE_MAINTENANT — rank 6.611 — opportunité 8.478 — entrée 6.850 — trend 5.250

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XDC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.365
2. MAGIC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.829
3. CRO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.729

## Accélération indépendante

- LINEA-EUR — BUILDING_ACCELERATION — score 6.011/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RUNE-EUR — BUILDING_ACCELERATION — score 5.924/10 — DETECTED_BUT_TOO_LATE
- IKA-EUR — BUILDING_ACCELERATION — score 5.896/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BOB-EUR — BUILDING_ACCELERATION — score 5.338/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QNT-EUR — BUILDING_ACCELERATION — score 5.023/10 — DETECTED_BUT_TOO_LATE
- CC-EUR — BUILDING_ACCELERATION — score 4.934/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GROVE-EUR — BUILDING_ACCELERATION — score 4.879/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 4.836/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 2Z-EUR — BUILDING_ACCELERATION — score 4.816/10 — DETECTED_BUT_TOO_LATE
- ALGO-EUR — BUILDING_ACCELERATION — score 4.766/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XDC-EUR — ACTIVE_NOW — score mémoire 8.365/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CC-EUR — ACTIVE_NOW — score mémoire 7.112/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- IMU-EUR — MEMORY_24H — score mémoire 9.209/10 — sources ACCELERATION — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- MAGIC-EUR — ACTIVE_NOW — score mémoire 7.829/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.773/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CRO-EUR — ACTIVE_NOW — score mémoire 7.729/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- HBAR-EUR +37.99% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +35.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALGO-EUR +15.26% — DETECTED_EARLY — couche NONE — action NONE
- IKA-EUR +14.83% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- MIOTA-EUR +14.54% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NMR-EUR +9.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MON-EUR +9.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XDC-EUR +8.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LINK-EUR +7.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +6.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
