# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T05:58:29.826125+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 8.048 | entrée 7.000 | trend 8.550 | rang 7.766
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SKY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.180 | entrée 6.000 | trend 8.750 | rang 7.873
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : HUMA-EUR | action LATENT_ACCELERATOR | opportunité 7.648 | entrée 5.550 | trend 8.450 | rang 7.457
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.368 | entrée 6.350 | trend 8.650 | rang 7.965
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. KAS-EUR — ACHETE_MAINTENANT — rank 7.766 — opportunité 8.048 — entrée 7.000 — trend 8.550
2. LTC-EUR — ACHETE_MAINTENANT — rank 7.638 — opportunité 8.075 — entrée 7.850 — trend 8.150
3. HBAR-EUR — ACHETE_MAINTENANT — rank 7.477 — opportunité 8.715 — entrée 7.650 — trend 6.750

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.965
2. SKY-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.873
3. CC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.872

## Accélération indépendante

- GRASS-EUR — CONFIRMED_ACCELERATION — score 6.879/10 — DETECTED_BUT_TOO_LATE
- HBAR-EUR — CONFIRMED_ACCELERATION — score 6.843/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XDC-EUR — CONFIRMED_ACCELERATION — score 6.720/10 — DETECTED_BUT_TOO_LATE
- MMT-EUR — BUILDING_ACCELERATION — score 6.461/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ROBO-EUR — BUILDING_ACCELERATION — score 6.380/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VIRTUAL-EUR — BUILDING_ACCELERATION — score 6.349/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — BUILDING_ACCELERATION — score 6.347/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRAM-EUR — BUILDING_ACCELERATION — score 6.321/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MANTRA-EUR — BUILDING_ACCELERATION — score 5.805/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- METIS-EUR — BUILDING_ACCELERATION — score 5.787/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- KAS-EUR — ACTIVE_NOW — score mémoire 7.766/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- HBAR-EUR — ACTIVE_NOW — score mémoire 7.477/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DGB-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.828/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.447/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 7.967/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.965/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SAFE-EUR — MEMORY_24H — score mémoire 7.933/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +54.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +35.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +18.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AUDIO-EUR +17.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +16.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +13.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XDC-EUR +12.97% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- GRASS-EUR +12.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IRYS-EUR +12.39% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- ARX-EUR +11.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
